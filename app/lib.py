import os
from fastapi import FastAPI
from pyrepositories import DataSource
from crud import CRUDApi

def init_project():
    """Initializes the project by creating the data directory if it doesn't exist."""

    project_root = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(project_root, "data")

    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    return data_dir


def bootstrap(data_source: DataSource) -> tuple[CRUDApi, FastAPI]:
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

    return CRUDApi(data_source, app), app
