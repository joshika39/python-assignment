import uvicorn
from pyrepositories import DataSource, JsonTable
import os
import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(os.path.join(path_root))

from app.lib import init_project, bootstrap
from app.models import Event, Organizer, Joiner, EventEntity

def main():
    """Main entry point of the application."""

    # NOTE: Initialize the project
    data_dir = init_project()
    data_source = DataSource()

    # NOTE: Create the tables
    events_table = JsonTable("events", data_dir)
    organizers_table = JsonTable("organizers", data_dir)

    # NOTE: Add the tables to the data source
    data_source.add_table(events_table)
    data_source.add_table(organizers_table)
    api, app = bootstrap(data_source)

    # NOTE: Register the CRUD routers
    api.add_router('events', Event)
    api.add_router('organizers', Organizer)

    # NOTE: Register the custom routers
    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    uvicorn.run(app, host="0.0.0.0", port=1234)

if __name__ == "__main__":
    main()

