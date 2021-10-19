from pydantic import BaseModel

class Speech(BaseModel):
    text: str
