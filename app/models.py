from pydantic import BaseModel
from typing import Optional

class SequenceEnrollment(BaseModel):
    contact_email: str
    contact_name: str
    campaign_name: str

class SequenceStatus(BaseModel):
    contact_email: str
    current_stage: int
    status: str # ACTIVE, PAUSED_REPLY_DETECTED, COMPLETED
    next_follow_up_message: Optional[str] = None
