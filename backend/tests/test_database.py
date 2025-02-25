from database import tasks_collection

def test_insert_task():
    task = {"title": "Insert tests", "done": False}
    result = tasks_collection.insert_one(task)
    assert result.acknowledged == True

def test_get_task_by_id():
    task = {"title": "Get Task Test", "done": False}
    result = tasks_collection.insert_one(task)
    task_id = result.inserted_id

    retrived_task = tasks_collection.find_one({"_id": task_id})
    assert retrived_task is not None
    assert retrived_task["title"] == "Get Task Test"

def test_update_task():
    task = {"title": "Update Task Test", "done": False}
    result = tasks_collection.insert_one(task)
    task_id = result.inserted_id

    tasks_collection.update_one({"_id": task_id}, {"$set": {"done": True}})
    updated_task = tasks_collection.find_one({"_id": task_id})

    assert updated_task["done"] is True

def test_delete_task():
    task = {"title": "Delete Task Test", "done": False}
    result = tasks_collection.insert_one(task)
    task_id = result.inserted_id

    tasks_collection.delete_one({"_id": task_id})
    deleted_task = tasks_collection.find_one({"_id": task_id})

    assert deleted_task is None