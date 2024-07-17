from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from app.domain.entities.messages import Chat
from app.domain.values.messages import Title
from app.infra.repositories.messages import BaseChatRepository
from app.logic.commands.base import BaseCommand, CommandHandler
from app.logic.exceptions.messages import ChatWithThatTitleAlreadyExistsException


@dataclass(frozen=True)
class CreateChatCommand(BaseCommand):
    title: str


@dataclass(frozen=True)
class CreateChatCommandHandler(CommandHandler[CreateChatCommand]):
    chat_repository: BaseChatRepository

    def handle(self, command: CreateChatCommand) -> Chat:
        if self.chat_repository.check_chat_exists_by_title(command.title):
            raise ChatWithThatTitleAlreadyExistsException(command.title)
        title = Title(value=command.title)
        return Chat.create_chat(title=title)
