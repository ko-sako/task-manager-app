from database import tasks_collection

def test_insert_task():
    task = {"title": "First tests", "done": False}
    result = tasks_collection.insert_one(task)
    assert result.acknowledged == True
