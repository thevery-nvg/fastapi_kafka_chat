from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable

from app.domain.events.base import BaseEvent
from app.logic.commands.base import CommandHandler, CT, CR, BaseCommand
from app.logic.events.base import EventHandler, ET, ER
from app.logic.exceptions.mediator import EventHandlersNotRegistered, CommandHandlersNotRegistered


@dataclass(eq=False)
class Mediator:
    events_map: dict[ET, EventHandler] = field(
        default_factory=lambda: defaultdict[list],
        kw_only=True
    )
    commands_map: dict[CT, CommandHandler] = field(
        default_factory=lambda: defaultdict[list],
        kw_only=True
    )

    def register_event(self, event: ET, event_handlers: Iterable[EventHandler[ET, ER]]):
        self.events_map[event.__class__] = event_handlers

    def register_command(self, command: CT, command_handlers: Iterable[CommandHandler[CT, CR]]):
        self.commands_map[command.__class__] = command_handlers

    def handle_event(self, event: BaseEvent) -> Iterable[ER]:
        event_type = event.__class__
        handlers = self.events_map.get(event_type)
        if not handlers:
            raise EventHandlersNotRegistered(event_type)
        return [handler.handle(event) for handler in handlers]

    def handle_commands(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.events_map.get(command_type)
        if not handlers:
            raise CommandHandlersNotRegistered(command_type)
        return [handler.handle(command) for handler in handlers]
