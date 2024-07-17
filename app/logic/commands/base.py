from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic, Any


@dataclass(frozen=True)
class BaseCommand(ABC):
    ...


CT = TypeVar("CT", bound=BaseCommand)
CR = TypeVar("CR", bound=Any)


@dataclass(frozen=True)
class CommandHandler(ABC, Generic[CT, CR]):
    a: CT
    b: CR

    @abstractmethod
    def handle(self, command: CT) -> CR:
        ...
