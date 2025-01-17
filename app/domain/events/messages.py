from dataclasses import dataclass

from app.domain.events.base import BaseEvent


@dataclass(kw_only=True)
class NewMessageReceivedEvent(BaseEvent):
    message_text: str
    message_oid: str
    chat_oid: str


@dataclass(kw_only=True)
class NewChatCreated(BaseEvent):
    chat_oid: str
    chat_title: str
