from flask import Flask, request, jsonify
from datetime import datetime

#local imports
from config import app_config 
from app.models.questions import QuestionsOp 

question = QuestionsOp('title', 'description', 'body')

def create_app(config_name):
 
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    
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

    return app 