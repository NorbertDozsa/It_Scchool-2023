from pydantic import BaseModel
import uuid

class Convert(BaseModel):

    status: str
    message: str
    video_id: str
    task_id: str
    url: str


class Url(BaseModel):

    url: str
