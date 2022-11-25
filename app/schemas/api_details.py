from pydantic import BaseModel


class APIDetails(BaseModel):
    project_name: str
    api_version: str
    model_version: str
