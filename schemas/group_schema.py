from pydantic import BaseModel
class GroupReq(BaseModel):
    name: str
    study_time: int
class GroupRes(BaseModel):
    id: int
    name: str
    study_time: int

    class Config:
        orm_mode = True,
        from_attributes = True