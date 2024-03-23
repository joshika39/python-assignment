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
        events = api.get_datasource().get_all("events")  #type: list[Event]
        return analyser.get_joiners_multiple_meetings(events)

def main():
    data_dir = init_project()
    data_source = DataSource()
    events_table = JsonTable("events", data_dir)
    organizers_table = JsonTable("organizers", data_dir)
    data_source.add_table(events_table)
    data_source.add_table(organizers_table)
    api = bootstrap(data_source)
    api.include_router('organizers', Organizer)
    events_router = api.register_router('events', Event)
    app = api.get_app()
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    setup_event_router(api, events_router.get_base())
    api.publish()
    uvicorn.run(app, host="0.0.0.0", port=1234)

if __name__ == "__main__":
    main()

