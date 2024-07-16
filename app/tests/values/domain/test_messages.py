from datetime import datetime
import pytest
from app.domain.entities.messages import Message, Chat
from app.domain.events.messages import NewMessageReceivedEvent
from app.domain.exceptions.messages import TitleTooLongException, EmptyTextException
from app.domain.values.messages import Text, Title
import faker


def test_create_message_short_success():
    text = Text('Hello world')
    message = Message(text)
    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_message_long_success():
    text = Text('Hello world' * 100)
    message = Message(text)
    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_message_empty():
    with pytest.raises(EmptyTextException):
        text = Text('')


def test_create_chat_success():
    title = Title('title')
    chat = Chat(title=title)

    assert chat.title == title
    assert not chat.messages
    assert chat.created_at.date() == datetime.today().date()


def test_create_chat_long_title():
    with pytest.raises(TitleTooLongException):
        title = Title('title' * 200)


def test_add_chat_message():
    text = Text('Hello world')
    message = Message(text)

    title = Title('title')
    chat = Chat(title=title)

    chat.add_message(message)

    assert message in chat.messages


def test_new_message_events():
    text = Text('Hello world')
    message = Message(text)

    title = Title('title')
    chat = Chat(title=title)
    chat.add_message(message)
    events = chat.pull_events()
    pulled_events = chat.pull_events()

    assert not pulled_events, pulled_events
    assert len(events) == 1, events
    new_event = events[0]
    assert isinstance(new_event, NewMessageReceivedEvent), new_event
    assert new_event.message_oid == message.oid
    assert new_event.message_text == message.text.as_generic_type()
    assert new_event.chat_oid == chat.oid
