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

    def test_user_can_fetch_all_questions(self):
        """
        Tests user can get all questions he/she has asked.
        """
        response = self.client.get("/questions",
                                data=json.dumps(dict()),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.data.decode("UTF-8"))

    def test_user_can_get_one_question_by_id(self):
        """
        Tests a user can get a question by id.
        """

        response = self.client.post("/questions",
                                 data=json.dumps(dict(
                                 title="test-title",
                                 description="test-descriptiont",
                                 body="test-body")),
                                 content_type="application/json")

        response = self.client.get("/questions/1",
                                 data=json.dumps(dict(qsn_id=1)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Ok", response_msg["Status"])

    def test_user_can_not_get_question_by_id_that_does_not_exist(self):
        response = self.client.get("questions/5",
                                 data=json.dumps(dict(qsn_id=5)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Error", response_msg["Status"])

    def test_user_can_post_question(self):
        """
        Tests a user can post a question.
        """
        response = self.client.post("/questions",
                                 data=json.dumps(self.question),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Question posted successfully", response_msg["Message"])