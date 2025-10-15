from pydantic import BaseModel
class StudyTimeReq(BaseModel):
    name: str
class StudyTimeRes(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True