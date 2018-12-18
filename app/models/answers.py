from datetime import datetime

class AnswerOp():
    def __init__(self, ans_body):
        self.ans_body = ans_body
        self.timeposted = datetime.now()
        self.Answers = []

    def post_new_answer(self, ans_id, ans_body, timeposted):
        new_answer = { 
            "ans_id": ans_id,
            "ans_body": ans_body, 
            "timeposted": timeposted
        }

        self.Answers.append(new_answer)

    def get_one_ans(self, ans_id):
        for i in self.Answers:
            if i['ans_id'] == ans_id:
                return i