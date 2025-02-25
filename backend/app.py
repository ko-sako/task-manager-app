from flask import Flask, jsonify, request
from database import tasks_collection

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Task Manager API"}, 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = list(tasks_collection.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True)

