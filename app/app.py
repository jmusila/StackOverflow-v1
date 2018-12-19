from flask import Flask, request, jsonify
from datetime import datetime

#local imports
from config import app_config
from app.models.answers import AnswerOp
from app.models.questions import QuestionsOp
from app.common.validators import validate_question, validate_answer 

question = QuestionsOp('title', 'description', 'body')
answer = AnswerOp('ans_body')

def create_app(config_name):
 
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    
    @app.route("/questions", methods=['GET'])
    def all_questions():
        return jsonify({"Questions": question.Questions}), 200

    @app.route("/questions", methods=['POST'])
    def add_question():
        data = request.get_json()
        qsn_id = len(question.Questions) + 1
        title = data['title']
        description = data['description']
        body = data['body']
        timeposted = question.timeposted
        question.post_new_question(qsn_id, title, description, body, timeposted)
        question_validator = validate_question(data) 

        if(question_validator != True):
            return question_validator 
        return jsonify({"Message": "Question posted successfully"}), 201

    @app.route("/questions/<int:qsn_id>", methods=['GET'])
    def get_single_question(qsn_id):
        i = question.get_one_question(qsn_id)
        if i:
            return jsonify({"Status": "Ok", "Question": i}), 200
        return jsonify({"Message" : "Question with that question_id not found", "Status" : "Error"}), 404 

    @app.route("/questions/<int:qsn_id>", methods=['DELETE'])
    def delete_question(qsn_id):
        k = question.get_one_question(qsn_id)
        if k:
            question.Questions.remove(k)
            return jsonify({"Message": "Question Deleted Successfully"}), 200
        return jsonify({"Message" : "Question with that question_id not found", "Status" : "Error"}), 404

    @app.route("/questions/<int:qsn_id>/answers", methods=['GET'])
    def all_answers(qsn_id):
        for j in question.Questions:
            if j['qsn_id'] == qsn_id:
                return jsonify({"Answers": answer.Answers}), 200
            return jsonify({"Message" : "Question with that question_id not found", "Status" : "Error"}), 404

    @app.route("/questions/<int:qsn_id>/answers", methods=['POST'])
    def post_answer(qsn_id):
        i = question.get_one_question(qsn_id)
        if i:
            data = request.get_json()
            ans_id = len(answer.Answers) + 1
            ans_body = data['ans_body']
            timeposted = answer.timeposted
            answer.post_new_answer(ans_id, ans_body, timeposted) 
            answer_validator = validate_answer(data)

            if(answer_validator != True):
                return answer_validator 
            return jsonify({'Message': "The Answer was added successfully", "Status": "Ok", }), 201
        return jsonify({"Message": "Question with that id not found"}), 404

    @app.route("/questions/<int:qsn_id>/answers/<int:ans_id>", methods=['GET'])
    def get_single_answer(qsn_id, ans_id):
        for i in question.Questions:
            if i['qsn_id'] == qsn_id:
                j = answer.get_one_ans(ans_id)
                if j:
                    return jsonify({"Status": "Ok", "Answer": j}), 200
                return jsonify({"Message" : "Answer with that id not found", "Status" : "Error"}), 404 
            return jsonify({"Message" : "Question with that id not found", "Status" : "Error"}), 404 

    @app.route("/questions/<int:qsn_id>/answers/<int:ans_id>", methods=['DELETE'])
    def delete_answer(qsn_id, ans_id):
        for i in question.Questions:
            if i['qsn_id'] == qsn_id:
                j = answer.get_one_ans(ans_id)
                if j:
                    answer.Answers.remove(j)
                    return jsonify({"Status": "Ok", "Message": "Answer deleted successfully"}), 204
                return jsonify({"Message" : "Answer with that id not found", "Status" : "Error"}), 404 
            return jsonify({"Message" : "Question with that id not found", "Status" : "Error"}), 404
        pass

    return app 