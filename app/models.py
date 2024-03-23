from crud import Model
from pyrepositories import Entity
from typing import List, Optional


class Organizer(Model):
    email: str


class Joiner(Model):
    name: str
    company: str


class Event(Model):
    date: str
    organizer: Organizer
    status: str
    max_attendees: int
    joiners: Optional[List[Joiner]] = None


class EventEntity(Entity):
    @property
    def date(self):
        return self.fields.get("date")
    @date.setter
    def date(self, value):
        self.fields["date"] = value
    @property
    def organizer(self):
        return self.fields.get("organizer")
    @organizer.setter
    def organizer(self, value):
        self.fields["organizer"] = value
    @property
    def status(self):
        return self.fields.get("status")
    @status.setter
    def status(self, value):
        self.fields["status"] = value
    @property
    def max_attendees(self):
        return self.fields.get("max_attendees")
    @max_attendees.setter
    def max_attendees(self, value):
        self.fields["max_attendees"] = value
    @property
    def joiners(self):
        return self.fields.get("joiners") or []
    @joiners.setter
    def joiners(self, value):
        self.fields["joiners"] = value
