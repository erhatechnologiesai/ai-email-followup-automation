SEQUENCES = {}

TEMPLATES = {
    1: "Just following up on my previous note regarding our autonomous AI automation mesh.",
    2: "Sharing a recent case study on how we reduced workflow execution latency by 40%.",
    3: "Final touchpoint: Should we pause outreach or revisit this in Q1?"
}

def enroll(email: str, name: str, camp: str):
    SEQUENCES[email] = {"name": name, "stage": 1, "status": "ACTIVE"}
    return 1, "ACTIVE", TEMPLATES[1]

def record_reply_detected(email: str):
    if email in SEQUENCES:
        SEQUENCES[email]["status"] = "PAUSED_REPLY_DETECTED"
        return True
    return False
