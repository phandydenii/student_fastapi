from pydantic import BaseModel

class ScoreReq(BaseModel):
    student_group_id: int
    subject_id: int
    month: int
    year: int
    total: float

class ScoreRes(BaseModel):
    id: int
    student_group_id: int
    subject_id: int
    month: int
    year: int
    total: float


class Config:
        orm_mode = True,
        from_attributes = True
