from pydantic import BaseModel, AnyHttpUrl, ValidationError

class Convert(BaseModel):

    status: str
    message: str
    # video_id: object
    task_id: str
    url: AnyHttpUrl

