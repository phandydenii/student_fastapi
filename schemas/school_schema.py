from pydantic import BaseModel

class SchoolReq(BaseModel):
    name_en: str
    name_km: str

class SchoolRes(BaseModel):
    id: int
    name_en: str
    name_km: str

    class Config:
        from_attributes = True
