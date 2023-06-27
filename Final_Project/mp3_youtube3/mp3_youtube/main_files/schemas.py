from pydantic import BaseModel
import uuid

class Convert(BaseModel):

    status: str
    message: str
    video_id: object
    task_id: str
    