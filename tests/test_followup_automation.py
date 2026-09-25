import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestFollowupAutomation(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_sequence_lifecycle(self):
        email = "prospect@acmecorp.com"
        res = self.client.post("/enroll", json={"contact_email": email, "contact_name": "Dave", "campaign_name": "Enterprise Outbound"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["status"], "ACTIVE")
        
        # Detect reply and verify auto-pause
        res2 = self.client.post(f"/reply-detected?contact_email={email}")
        self.assertEqual(res2.status_code, 200)
        self.assertTrue(res2.json()["sequence_halted"])

if __name__ == "__main__":
    unittest.main()
