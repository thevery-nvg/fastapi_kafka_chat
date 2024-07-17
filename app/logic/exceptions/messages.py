from dataclasses import dataclass

from app.logic.exceptions.base import LogicException


@dataclass(frozen=True)
class ChatWithThatTitleAlreadyExistsException(LogicException):
    title: str

    @property
    def message(self):
        return f"Чат с таким названием уже существует {self.title}"
