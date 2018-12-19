import os 
import unittest
import json

#local imports
from app.app import create_app
from app.models.questions import QuestionsOp
from app.app import answer,question

class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

        self.question ={
            "title": "Computer Science",
            "description": "This is the description",
            "body": "I am the question body"
        }

    def test_question_empty_title(self):
        response = self.client.post("/questions", data=json.dumps(dict(title="",
        description="Thisid the", body="hgfdhg")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Question title is required",
                      response_msg["Message"])

    def test_post_question_empty_body(self):
        """
        Tests user cannnot add a question without body
        """
        response = self.client.post("/questions",
                                 data=json.dumps(dict(title="This is my title",
                                                      description="Desrcption", body="")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Question body is required",
                      response_msg["Message"])