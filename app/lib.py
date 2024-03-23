import os
from fastapi import FastAPI
from pyrepositories import DataSource
from crud import CRUDApi
from .models import Event


def init_project():
    """Initializes the project by creating the data directory if it doesn't exist."""

    project_root = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(project_root, "data")

    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    return data_dir


def bootstrap(data_source: DataSource) -> CRUDApi:
    app = FastAPI(
        title="My API",
        description="This is a very fancy project, with auto docs for the API and everything.",
        version="0.1.0",
        contact={
            "name": "John Doe",
            "url": "https://example.com",
            "email": "john@doe.com"
        },
        license_info={
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT"
        }
    )

    return CRUDApi(data_source, app)

def get_joiner_by_name(events, name):
    for event in events:
        for joiner in event.joiners or []:
            if joiner.name == name:
                return joiner

    return None


class EventAnalyzer:
    def get_joiners_multiple_meetings(self, events: list[Event]) -> list[dict]:
        """Returns a list of joiners, who have joined at least two meetings."""
        joiners = {}
        for event in events:
            for joiner in event.joiners or []:
                name = joiner.name
                if name in joiners:
                    joiners[name] += 1
                else:
                    joiners[name] = 1

        j_list = []
        for event in events:
            for joiner in event.joiners or []:
                name = joiner.name
                if joiners[name] >= 2:
                    j_list.append(get_joiner_by_name(events, name))

        return j_list

