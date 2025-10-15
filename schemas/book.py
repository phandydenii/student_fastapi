from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    description: str

class BookCreate(BaseModel):
    title: str
    author: str

class BookResponse(BaseModel):
    id: int
    title: str
    author: str


    class Config:
        orm_mode = True,
        from_attributes = True
