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