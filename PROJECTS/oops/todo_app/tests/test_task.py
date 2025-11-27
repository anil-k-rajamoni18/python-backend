from todo.task import Task

def test_task_creation():
    t = Task("Test Task", "Description", "Work", 5, "2025-06-07 10:00")
    assert t.title == "Test Task"
    assert t.completed is False
    t.mark_complete()
    assert t.completed is True
