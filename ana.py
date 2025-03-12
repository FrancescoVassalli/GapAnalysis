import logging
from typing import List

from fastapi import APIRouter, Request
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


@router.get("/fetch-linkedin-page/{url}")
async def fetch_linkedin_page(request: Request, url: str):
    return request_linkedin_html(url)


@router.get("/valid-targets/")
async def bait(request: Request) -> List[str]:
    target_names = list(target_homepage_dict.keys())
    target_names.remove('jeremy')
    return target_names


@router.get("/bait/{target_name}")
async def bait(request: Request, target_name: str):
    content = create_bait(target_name)
    db: Database = request.app.state.db
    with db.get_session() as session:
        bait = Bait(name=target_name, content=content)
        session.add(bait)
        session.commit()
        session.refresh(bait)
        return {bait.id: bait.content}


@router.get("/email-html/{target_name}")
async def get_email_html(request: Request, target_name: str):
    return complete_email_html(target_homepage_dict[target_name])


@router.get("/welcome")
async def welcome(request: Request):
    return "Welcome"


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
        return first_ai_response


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
        return new_ai_message


@router.get("/all-bait-chat/{bait_id}")
async def get_all_chats_for_bait(request: Request, bait_id: int) -> str:
    db: Database = request.app.state.db
    with db.get_session() as session:
        return collect_chats_in_paragraph_format(session, bait_id)


@router.get("/summary")
async def get_summary(request: Request) -> str:
    db: Database = request.app.state.db
    with db.get_session() as session:
        return summarize(session)
