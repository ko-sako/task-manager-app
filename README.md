# Task Management App
A simple task management app built with **Python (Flask) & MongoDB (NoSQL)**, following Test-Driven Development (TDD) principles.

---

## Tech Stack
1st Sprint
- **Backend:** Flask, Flask-PyMongo, Flask-CORS
- **Database:** MongoDB (NoSQL)
- **Testing:** Pytest

2nd Sprint (TBC)
- **Frontend:** React, TypeScript, Axios
- **Deployment:** AWS Lambda, Vercel  

## Interact with the API Using Postman
### Create a Task
POST request to `http://localhost:5000/tasks`

Request Body (in JSON format):

```json
{
  "title": "Write API documentation",
  "done": false
}
```

Response: get a response with the task's ID `inserted_task_id`

```json
{
  "id": "inserted_task_id"
}
```

### Get All Tasks
GET request to http://localhost:5000/tasks

Response: return a list of tasks stored in the database. Each task will include the title and done status.

```json
[
  {
    "_id": "inserted_task_id",
    "title": "Write API documentation",
    "done": false
  }
]
```

### Update a Task
PUT request to http://localhost:5000/tasks/<task_id>

Replace <`task_id`> with the actual ID of the completed task

Request Body (in JSON format):

```json
{
  "done": true
}
```

Response: This updates the task with the specified ID to mark it as complete (done: true).

```json
{
  "message": "Task updated successfully"
}
```

### Delete a Task
DELETE request to http://localhost:5000/tasks/<task_id>

Replace <task_id> with the ID of the task you want to delete.

Response: This will delete the task with the given ID.

```json
{
  "message": "Task deleted successfully"
}
```
