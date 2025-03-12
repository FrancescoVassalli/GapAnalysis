import logging
from typing import List

from fastapi import APIRouter, Request
from pydantic import BaseModel
from sqlmodel import delete, select

from db import Database
from interview_interface import begin_interview, continue_interview
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
async def valid_targets(request: Request) -> List[str]:
    target_names = list(target_homepage_dict.keys())
    target_names.remove('jeremy')
    return ValidTargetsResponse(targets=target_names)


class ActiveBaitsResponse(BaseModel):
    active_baits: List[Bait]


@router.get("/active-baits/")
async def get_active_baits(request: Request) -> List[Bait]:
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


@router.post("/start-chat/{bait_id}")
async def start_chat(request: Request, bait_id: int) -> str:
    db: Database = request.app.state.db
    with db.get_session() as session:
        session.exec(delete(ChatHistory).where(ChatHistory.bait_id == bait_id))
        session.commit()
        db_bait: Bait = session.query(Bait).where(Bait.id == bait_id).one()
        first_chat: ChatHistory = ChatHistory(
            message=db_bait.content, sender=Sender.HUMAN, bait_id=db_bait.id
        )
        first_ai_response = begin_interview(db_bait.content)
        first_ai_chat: ChatHistory = ChatHistory(
            message=first_ai_response, sender=Sender.AI, bait_id=db_bait.id
        )
        session.add(first_chat)
        session.add(first_ai_chat)
        session.commit()
        return StartChatResponse(response=first_ai_response)


class AddChatResponse(BaseModel):
    response: str


@router.post("/add-chat/{bait_id}/{user_message}")
async def add_chat(request: Request, bait_id: int, user_message: str) -> str:
    db: Database = request.app.state.db
    with db.get_session() as session:
        old_chats: List[ChatHistory] = (
            session.query(ChatHistory).where(ChatHistory.bait_id == bait_id).all()
        )
        new_user_chat: ChatHistory = ChatHistory(
            message=user_message, sender=Sender.HUMAN, bait_id=bait_id
        )
        session.add(new_user_chat)
        old_chats.append(new_user_chat)
        new_ai_message = continue_interview(old_chats)
        new_ai_chat: ChatHistory = ChatHistory(
            message=new_ai_message, sender=Sender.AI, bait_id=bait_id
        )
        session.add(new_ai_chat)
        session.commit()
        return AddChatResponse(response=new_ai_message)


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
    content: str


@router.get("/all-bait-chat/{bait_id}", response_model=AllBaitChatResponse)
async def get_all_chats_for_bait(request: Request, bait_id: int) -> AllBaitChatResponse:
    db: Database = request.app.state.db
    with db.get_session() as session:
        content = collect_chats_in_paragraph_format(session, bait_id)
        return AllBaitChatResponse(content=content)


class SummaryResponse(BaseModel):
    summary: str


@router.get("/summary", response_model=SummaryResponse)
async def get_summary(request: Request) -> SummaryResponse:
    db: Database = request.app.state.db
    with db.get_session() as session:
        summary = summarize(session)
        return SummaryResponse(summary=summary)
