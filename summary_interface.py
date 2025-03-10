import json
from typing import Collection, List

from sqlmodel import Session, select

from models import Bait, ChatHistory


def adapt_chat_history_to_paragraph(chat: ChatHistory) -> str:
    return f'{chat.sender}: {chat.message}'


def collect_chats_in_paragraph_format(session: Session, bait_id: int) -> str:
    old_chats: List[ChatHistory] = (
        session.query(ChatHistory).where(ChatHistory.bait_id == bait_id).all()
    )
    # the first chat is the bait email so I take that out here
    old_chats.sort(key=lambda chat: chat.created_at)
    old_chats.pop(0)
    chat_paragraphs = [adapt_chat_history_to_paragraph(chat) for chat in old_chats]
    return '\n'.join(chat_paragraphs)


def add_interview_header(interview: str, bait_id: int) -> str:
    return f'User {bait_id} clicked on a bait phising email and then this interview was conducted by a cybersecurity assistant:\n{interview}'


def summarize(session: Session, baits: Collection[int] = None):
    '''@param baits a collection of bait_ids to use for the summary. If left blank all are used.'''
    if baits is None:
        baits: List[int] = session.exec(select(Bait.id)).all()
    chat_paragraphs = [
        add_interview_header(
            collect_chats_in_paragraph_format(session, bait_id), bait_id
        )
        for bait_id in baits
    ]
    return json.dumps(chat_paragraphs)
