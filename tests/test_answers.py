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