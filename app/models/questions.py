from datetime import datetime


class QuestionsOp():
    def __init__(self, title, description, body):
        self.title = title
        self.description = description
        self.body = body
        self.timeposted = datetime.now()
        self.Questions = []

    def post_new_question(self, qsn_id, title, description, body, timeposted):
        new_qsn = {
            "qsn_id": qsn_id,
            "title": title,
            "description": description,
            "body": body,
            "time": timeposted
        }

        self.Questions.append(new_qsn)

    def get_one_question(self, qsn_id):
        for i in self.Questions:
            if i['qsn_id'] == qsn_id:
                return i
        pass