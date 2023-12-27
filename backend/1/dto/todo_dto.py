from pydantic import BaseModel


class TodoDto(BaseModel):
    title: str
    content: str
