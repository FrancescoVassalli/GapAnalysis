import json
import logging
from typing import Iterator, List, Literal

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from sqlmodel import delete, distinct, select

from db import Database
from interview_interface import begin_interview, stream_continue_interview_from_dicts
from models import Bait, ChatHistory, Sender
from phish_interface import (
    complete_email_html,
    create_bait,
    request_linkedin_html,
    target_homepage_dict,
)
from summary_interface import collect_chats_in_paragraph_format, summarize

logger = logging.getLogger('router')

router = APIRouter(
    prefix="/mock",
    tags=["mock"],
    responses={404: {"description": "Not found"}},
)


class ValidTargetsResponse(BaseModel):
    targets: List[str]


@router.get("/valid-targets/")
async def valid_targets(
    request: Request, response_model=ValidTargetsResponse
) -> ValidTargetsResponse:
    target_names = list(target_homepage_dict.keys())
    target_names.remove('jeremy')
    return ValidTargetsResponse(targets=target_names)


class TotalBaitsResponse(BaseModel):
    count: int


@router.get("/total-baits/", response_model=TotalBaitsResponse)
async def get_total_baits(request: Request) -> TotalBaitsResponse:
    db: Database = request.app.state.db
    with db.get_session() as session:
        return TotalBaitsResponse(count=len(session.exec(select(Bait)).all()))


@router.get("/total-chat-sessions/", response_model=TotalBaitsResponse)
async def get_total_chat_sessions(request: Request) -> TotalBaitsResponse:
    db: Database = request.app.state.db
    with db.get_session() as session:
        baits: List[int] = session.exec(select(ChatHistory.bait_id)).all()
        baits_unique = set(baits)
        return TotalBaitsResponse(count=len(baits_unique))


class ActiveBaitsResponse(BaseModel):
    active_baits: List[Bait]


@router.get("/active-baits/", response_model=ActiveBaitsResponse)
async def get_active_baits(request: Request) -> ActiveBaitsResponse:
    db: Database = request.app.state.db
    with db.get_session() as session:
        return ActiveBaitsResponse(active_baits=session.exec(select(Bait)).all())


class LinkedInPageResponse(BaseModel):
    content: str


@router.get("/fetch-linkedin-page/{url}", response_model=LinkedInPageResponse)
async def fetch_linkedin_page(request: Request, url: str):
    content = request_linkedin_html(url)
    return LinkedInPageResponse(content=content)


class BaitResponse(BaseModel):
    id: int
    content: str


@router.get("/bait/{target_name}", response_model=BaitResponse)
async def bait(request: Request, target_name: str):
    content = create_bait(target_name)
    db: Database = request.app.state.db
    with db.get_session() as session:
        bait = Bait(name=target_name, content=content)
        session.add(bait)
        session.commit()
        session.refresh(bait)
        return BaitResponse(id=bait.id, content=bait.content)


class EmailHTMLResponse(BaseModel):
    content: str


@router.get("/email-html/{target_name}", response_model=EmailHTMLResponse)
async def get_email_html(request: Request, target_name: str):
    content = complete_email_html(target_homepage_dict[target_name])
    return EmailHTMLResponse(content=content)


class WelcomeResponse(BaseModel):
    message: str


@router.get("/welcome", response_model=WelcomeResponse)
async def welcome(request: Request):
    return WelcomeResponse(message="Welcome")


class StartChatResponse(BaseModel):
    response: str


@router.post("/start-chat/{bait_id}", response_model=StartChatResponse)
async def start_chat(request: Request, bait_id: int) -> StartChatResponse:
    db: Database = request.app.state.db
    with db.get_session() as session:
        # Clear previous chat history.
        session.exec(delete(ChatHistory).where(ChatHistory.bait_id == bait_id))
        session.commit()
        db_bait: Bait = session.query(Bait).where(Bait.id == bait_id).one()

        # Create the initial user chat.
        first_chat: ChatHistory = ChatHistory(
            message=db_bait.content, sender=Sender.HUMAN, bait_id=db_bait.id
        )
        session.add(first_chat)

        first_ai_response = begin_interview()

        first_ai_chat: ChatHistory = ChatHistory(
            message=first_ai_response, sender=Sender.AI, bait_id=db_bait.id
        )
        session.add(first_ai_chat)
        session.commit()
        return StartChatResponse(response=first_ai_response)


class StreamAddChatResponse(BaseModel):
    response: str


class UserMessageRequest(BaseModel):
    user_message: str


@router.post(
    "/stream-add-chat/{bait_id}",
    summary="Stream add chat (final response)",
    response_class=StreamingResponse,
    responses={
        200: {
            "description": "A streaming response of chat tokens",
            "content": {
                "text/event-stream": {
                    "schema": {
                        "type": "string",
                        "example": (
                            "data: {\"data\": \"Hello\"}\n"
                            "\ndata: {\"data\": \"World\"}\n\n"
                        ),
                    }
                }
            },
        },
    },
)
def stream_add_chat(request: Request, bait_id: int, payload: UserMessageRequest):
    user_message = payload.user_message
    db = request.app.state.db

    # Save the user's message to the database.
    with db.get_session() as session:
        existing_chats = (
            session.query(ChatHistory).where(ChatHistory.bait_id == bait_id).all()
        )
        new_user_chat = ChatHistory(
            message=user_message, sender=Sender.HUMAN, bait_id=bait_id
        )
        session.add(new_user_chat)
        session.commit()
        existing_chats.append(new_user_chat)
        chats_dict = [chat.get_message_dict() for chat in existing_chats]

    # Create an initial (empty) record for the AI's streaming message.
    with db.get_session() as session:
        ai_chat = ChatHistory(message="", sender=Sender.AI, bait_id=bait_id)
        session.add(ai_chat)
        session.commit()
        ai_chat_id = ai_chat.id  # Ensure your ChatHistory model has an "id" attribute.

    def event_generator() -> Iterator[str]:
        accumulated_message = ""
        # Stream tokens from OpenAI.
        for token in stream_continue_interview_from_dicts(chats_dict):
            accumulated_message += token

            # Update the AI chat record incrementally with the new message.
            with db.get_session() as session:
                session.query(ChatHistory).filter(ChatHistory.id == ai_chat_id).update(
                    {"message": accumulated_message}
                )
                session.commit()

            # Format the token as a server-sent event.
            if token == "[END]":
                # Append a marker so the client knows the stream has ended.
                token_with_marker = token + " END STREAM"
                yield f"data: {json.dumps({'data': token_with_marker})}\n\n"
                break
            yield f"data: {json.dumps({'data': token})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")


class ChatResponse(BaseModel):
    id: int
    name: str
    path: str


# create api route to pull all chats for a user
@router.get("/chats", response_model=List[ChatResponse])
async def get_chats(request: Request):
    db: Database = request.app.state.db
    with db.get_session() as session:
        baits: List[Bait] = session.query(Bait).all()
        all_chats = [
            ChatResponse(id=bait.id, name=bait.name, path=f"/chat/{bait.id}")
            for bait in baits
        ]
        return all_chats


class AllBaitChatResponse(BaseModel):

    class Message(BaseModel):
        type: Literal["user", "assistant"]
        message: str

    messages: List[Message]


@router.get("/all-bait-chat/{bait_id}", response_model=AllBaitChatResponse)
async def get_all_chats_for_bait(request: Request, bait_id: int) -> AllBaitChatResponse:
    db: Database = request.app.state.db
    with db.get_session() as session:
        content = collect_chats_in_paragraph_format(session, bait_id)
        return AllBaitChatResponse(messages=content)


class SummaryResponse(BaseModel):
    summary: str


@router.get("/summary", response_model=SummaryResponse)
async def get_summary(request: Request) -> SummaryResponse:
    db: Database = request.app.state.db
    with db.get_session() as session:
        summary = summarize(session)
        return SummaryResponse(summary=summary)


class ActiveBaitResponse(BaseModel):
    bait: str


@router.get("/active-bait/{bait_id}", response_model=ActiveBaitResponse)
async def get_active_bait(request: Request, bait_id: int) -> ActiveBaitResponse:
    db: Database = request.app.state.db
    with db.get_session() as session:
        return ActiveBaitResponse(
            bait=session.query(Bait).where(Bait.id == bait_id).one().content
        )
