from dataclasses import dataclass, field
from app.domain.entities.base import BaseEntity
from app.domain.values.messages import Text, Title


@dataclass
class Message(BaseEntity):
    text: Text

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, other: 'Message') -> bool:
        return self.oid == other.oid


@dataclass
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True
    )

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, other: 'Chat') -> bool:
        return self.oid == other.oid

    def add_message(self, message: Message):
        self.messages.add(message)