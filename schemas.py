from pydantic import BaseModel, EmailStr
from typing import Optional

class TicketBase(BaseModel):
    customer_email: EmailStr
    subject: str
    message: str

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    subject: Optional[str] = None
    message: Optional[str] = None
    intent: Optional[str] = None
    urgency: Optional[str] = None
    priority: Optional[str] = None

class TicketResponse(TicketBase):
    id: int
    intent: str
    urgency: str
    priority: str
    confidence: Optional[float]

    class Config:
        from_attributes = True
