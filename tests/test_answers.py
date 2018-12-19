import os 
import unittest
import json

#local imports
from app.app import create_app
from app.models.answers import AnswerOp
from app.app import answer,question

class TestAnswers(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

        self.question ={
            "title": "Computer Science",
            "description": "This is the description",
            "body": "I am the question body"
        }

        self.answer = {
            "ans_body": "This is the question body"
        }

    def test_user_can_post_answer(self):
        """
        Tests a user can post answer to a question.
        """
        response = self.client.post("/questions",
                                    data=json.dumps(self.question),
                                    content_type="application/json")
        response = self.client.post("/questions/1/answers",
                                    data=json.dumps(self.answer),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("The Answer was added successfully", response_msg["Message"])