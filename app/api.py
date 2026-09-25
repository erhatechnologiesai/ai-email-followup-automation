from fastapi import FastAPI
from app.config import settings
from app.models import SequenceEnrollment, SequenceStatus
from app.services.sequence_engine import enroll, record_reply_detected

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/enroll", response_model=SequenceStatus)
def enroll_contact(req: SequenceEnrollment):
    stage, status, msg = enroll(req.contact_email, req.contact_name, req.campaign_name)
    return SequenceStatus(contact_email=req.contact_email, current_stage=stage, status=status, next_follow_up_message=msg)

@app.post("/reply-detected")
def reply_detected(contact_email: str):
    found = record_reply_detected(contact_email)
    return {"contact_email": contact_email, "sequence_halted": found}
