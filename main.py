from fastapi import APIRouter
import uvicorn
from pyrepositories import DataSource, JsonTable
from crud import CRUDApi
import os
import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(os.path.join(path_root))

from app.lib import init_project, bootstrap, EventAnalyzer
from app.models import Event, Organizer

def setup_event_router(api: CRUDApi, router: APIRouter):
    analyser = EventAnalyzer()
    @router.get("/events/joiners/multiple-meetings")
    async def get_multiple_meetings():
        events = api.datasource.get_all("events")  #type: list[Event]
        return analyser.get_joiners_multiple_meetings(events)

def main():
    data_dir = init_project()
    data_source = DataSource()
    events_table = JsonTable("events", data_dir)
    organizers_table = JsonTable("organizers", data_dir)
    data_source.add_table(events_table)
    data_source.add_table(organizers_table)
    api = bootstrap(data_source)
    api.add_router('organizers', Organizer)
    events_router = api.add_router('events', Event)
    e_r = events_router.get_base()

    @e_r.post("/join/{event_id}/{organizer_id}")
    async def join_event(event_id: str, organizer_id: str):
        print(f"Joining event {event_id} with organizer {organizer_id}")

    app = api.get_app()
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    setup_event_router(api, events_router.get_base())
    uvicorn.run(app, host="0.0.0.0", port=1234)

if __name__ == "__main__":
    main()

