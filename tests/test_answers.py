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

    def test_post_answer_with_invalid_question_id(self):
        """
        Tests user cannnot answer a question without body 
        """
        response = self.client.post("/questions/1/answers",
                                 data=json.dumps(self.answer),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Question with that id not found",
                      response_msg["Message"])

    def test_user_can_fetch_all_answers(self):
        """
        Tests user can get all answers he/she has given.
        """
        response = self.client.post("/questions",
                                    data=json.dumps(self.question),
                                    content_type="application/json")
        response = self.client.get("/questions/1/answers",
                                data=json.dumps(self.answer),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.data.decode("UTF-8"))

    def test_post_answer_with_qsn_id_that_does_not_exist(self):
        """
        Tests user cannnot answer a question that does not exist
        """
        response = self.client.post("/questions",
                                    data=json.dumps(self.question),
                                    content_type="application/json")

        response = self.client.post("/questions/5/answers",
                                 data=json.dumps(dict(qsn_id="5",
                                                      ans_body="wertghdfggdggdg")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Question with that id not found",
                      response_msg["Message"])

    def test_delete_answer(self):
        """
        Test user can delete their answers. (DELETE request).

        """
        response = self.client.post("/questions",
                                    data=json.dumps(self.question),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            "questions/1/answers", content_type='application/json', data=json.dumps(self.answer))
        self.assertEqual(response.status_code, 201)
        res = self.client.delete("questions/1/answers/1", content_type='application/json')
        self.assertEqual(res.status_code, 204)
        # Test to see if it exists, should return a 404
        result = self.client.get("questions/1/answers/1")
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        del question.Questions[:]
        del answer.Answers[:]
        pass