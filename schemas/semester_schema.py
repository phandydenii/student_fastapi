from datetime import datetime

from pydantic import BaseModel

class SemesterReq(BaseModel):
    no: int
    start: datetime
    end: datetime
class SemesterRes(BaseModel):
    id: int
    no: int
    start: datetime
    end: datetime

    class Config:
        orm_mode = True,
        from_attributes = True