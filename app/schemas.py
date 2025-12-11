from typing import Optional
from pydantic import BaseModel


class LeadBase(BaseModel):
    external_id: Optional[str] = None
    phone: Optional[str] = None


class LeadCreate(LeadBase):
    pass


class ContactCreate(BaseModel):
    lead: LeadBase
    source_name: str
    payload: dict


class ContactRead(BaseModel):
    id: int
    lead_id: int
    source_id: int
    operator_id: Optional[int]
    status: str
    payload: dict

    class Config:
        orm_mode = True
