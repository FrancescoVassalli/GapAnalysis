from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Column, DateTime
from enum import Enum

class BaitBase(SQLModel):
    name: str = Field(nullable=False)
    content: str = Field(nullable=False)

class Bait(BaitBase, table=True):
    __tablename__ = "bait"
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)

class Sender(str, Enum):
    HUMAN = "human"
    AI = "ai"

class ChatHistoryBase(SQLModel):
    message: str = Field(nullable=False)
    sender: str = Field(nullable=False)
    bait_id: int = Field(foreign_key="bait.id", index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, sa_column=Column(DateTime(timezone=True), nullable=False))

    def get_message_dict(self):
        sender_for_message = self.sender
        return {
            "type": sender_for_message,
            "data": {
                        "content": self.message or ""
                    },
        }

class ChatHistory(ChatHistoryBase, table=True):
    __tablename__ = "chat_history"
    __table_args__ = {'extend_existing': True}
    id: Optional[int] = Field(default=None, primary_key=True)

    @classmethod
    def from_base(cls, chat_history: ChatHistoryBase):
        return cls(**chat_history.dict())