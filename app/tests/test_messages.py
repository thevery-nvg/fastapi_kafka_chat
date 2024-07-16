from datetime import datetime
import pytest
from app.domain.entities.messages import Message, Chat
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


def add_chat_message():
    text = Text('Hello world')
    message = Message(text)

    title = Title('title')
    chat = Chat(title=title)

    chat.add_message(message)

    assert message in chat.messages
