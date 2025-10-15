from datetime import datetime

from pydantic import BaseModel

class PromotionReq(BaseModel):
    no: int
    start: datetime
    end: datetime

class PromotionRes(BaseModel):
    id: int
    no: int
    start: datetime
    end: datetime

    class Config:
        from_attributes = True