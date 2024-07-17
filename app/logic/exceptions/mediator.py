from dataclasses import dataclass

from app.logic.exceptions.base import LogicException


@dataclass(frozen=True, eq=False)
class EventHandlersNotRegistered(LogicException):
    event_type: type

    @property
    def message(self):
        return f"Не удалось найти обработчики для события {self.event_type}"


@dataclass(frozen=True, eq=False)
class CommandHandlersNotRegistered(LogicException):
    command_type: type

    @property
    def message(self):
        return f"Не удалось найти обработчики для команды {self.command_type}"
