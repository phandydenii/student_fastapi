from pydantic import BaseModel

class DegreeReq(BaseModel):
    name_en: str
    name_km: str

class DegreeRes(BaseModel):
    id: int
    name_en: str
    name_km: str

    class Config:
        orm_mode = True,
        from_attributes = True
