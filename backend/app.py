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

@app.route("/tasks", methods=["POST"])
def create_task():
    task_data = request.get_json()
    result = tasks_collection.insert_one(task_data)
    return jsonify({"id": str(result.inserted_id)}), 201

@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    task_data = request.get_json()
    tasks_collection.update_one({"_id": task_id}, {"$set": task_data})
    return jsonify({"message": "Task updated successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)

