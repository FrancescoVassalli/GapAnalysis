import json
from typing import Collection, List

from openai import OpenAI
from sqlmodel import Session, select

from google_reasoning_interface import complete_summary as google_complete_summary
from models import Bait, ChatHistory

client = OpenAI()


def adapt_chat_history_to_paragraph(chat: ChatHistory) -> str:
    return f'{chat.sender}: {chat.message}'


def collect_chats_in_paragraph_format(session: Session, bait_id: int) -> str:
    old_chats: List[ChatHistory] = session.exec(
        select(ChatHistory)
        .where(ChatHistory.bait_id == bait_id)
        .order_by(ChatHistory.created_at)
        .offset(1)  # Skip the first chat
    ).all()

    # if no old_chats return empty string
    if not old_chats:
        return []

    chat_paragraphs = [
        {
            "type": "user" if chat.sender == "user" else "assistant",
            "message": chat.message,
        }
        for chat in old_chats
    ]
    return chat_paragraphs


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
    return complete_summary(chat_paragraphs)


def complete_summary(chats: List[str]) -> str:
    # use google instead
    # completion = client.chat.completions.create(
    # model="gpt-4o",
    # messages=[
    # {
    # "role": "system",
    # "content": [
    # {
    # "type": "text",
    # "text": MAKE_SUMMARY_TEXT,
    # }
    # ],
    # },
    # {
    # "role": "user",
    # "content": [
    # {
    # "type": "text",
    # "text": json.dumps(chats),
    # }
    # ],
    # },
    # ],
    # response_format={"type": "text"},
    # temperature=1,
    # max_completion_tokens=2048,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0,
    # )
    # return completion.choices[0].message.content
    return google_complete_summary(chats)
