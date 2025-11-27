from todo.task_manager import TaskManager
from todo.task import Task

def test_add_get_task(db):
    manager = TaskManager("test_tasks.db")
    t = Task("Task 1", "Desc", "Home", 3, None)
    task_id = manager.add_task(t)
    assert task_id is not None
    fetched = manager.get_task(task_id)
    assert fetched.title == "Task 1"
    assert fetched.priority == 3

def test_update_task(db):
    manager = TaskManager("test_tasks.db")
    t = Task("Task 2", "Desc2", "Work", 4)
    tid = manager.add_task(t)
    t_fetched = manager.get_task(tid)
    t_fetched.title = "Updated Task 2"
    t_fetched.priority = 7
    manager.update_task(t_fetched)
    updated = manager.get_task(tid)
    assert updated.title == "Updated Task 2"
    assert updated.priority == 7

def test_delete_task(db):
    manager = TaskManager("test_tasks.db")
    t = Task("Task to delete", "Desc", "Misc", 1)
   
