from flask import Flask, request, jsonify
from datetime import datetime

#local imports
from config import app_config 
from app.models.questions import QuestionsOp
from app.common.validators import validate_question 

question = QuestionsOp('title', 'description', 'body')

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
        pass

    return app 