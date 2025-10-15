from pydantic import BaseModel

class StudentGroupReq(BaseModel):
    student_id: int
    group_id: int
    semester_id: int


class StudentGroupRes(BaseModel):
    id: int
    student_id: int
    group_id: int
    semester_id: int

    class Config:
        from_attributes = True