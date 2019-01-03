from flask import Flask, jsonify


def validate_question(json):
    if not(json["title"].strip()):
        return jsonify({"Message":"Question title is required"}), 401

    if not (json["description"].strip()):
        return jsonify({"Message":"Question description is required"}), 401

    if not (json["body"].strip()):
        return jsonify({"Message":"Question body is required"}), 401

    return True

def validate_answer(json):
    if not(json["ans_body"].strip()):
        return jsonify({"Message":"Answer body is required"}), 401

    return True