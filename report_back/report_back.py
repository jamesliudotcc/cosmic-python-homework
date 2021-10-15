from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel


class User(BaseModel):
    name: str
    phone: str
    id = str(uuid4())
    default_timezone = "PST"  # TODO fix


class Contact(BaseModel):
    name: str
    phone: str
    id = str(uuid4())

    def __hash__(self):
        return hash(id)


class FakeTextSender:
    pass


class Activity:
    def __init__(
        self,
        user: User,
        contacts: set[Contact],
        start_time=datetime.now(),
        end_time: datetime = None,
        started: datetime = None,
        ended: datetime = None,
        contacted: set[Contact] = set(),
        id=str(uuid4()),
    ):
        self.user = user
        self.contacts = contacts
        self.start_time = start_time
        self.end_time = end_time
        self.started = started
        self.ended = ended
        self.contacted = contacted
        self.id = id

    def __repr__(self) -> str:
        return f"Activity(user: {self.user}, contacts: {self.contacts}, ended: {self.ended}, contacted: {self.contacted})"

    def start(self) -> None:
        self.started = datetime.now()

    def end(self) -> None:
        self.ended = datetime.now()
