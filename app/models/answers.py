from datetime import datetime

class AnswerOp():
    def __init__(self, ans_body):
        self.ans_body = ans_body
        self.timeposted = datetime.now()
        self.Answers = []
        pass