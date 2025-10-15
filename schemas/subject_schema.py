from pydantic import BaseModel

class SubjectReq(BaseModel):
    name_en: str
    name_km: str
    grade_id: int

class SubjectRes(BaseModel):
    id: int
    name_en: str
    name_km: str
    grade_id: int

    class Config:
        from_attributes = True
