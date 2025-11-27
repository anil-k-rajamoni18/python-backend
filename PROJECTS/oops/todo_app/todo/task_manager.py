from todo.db import Database
from todo.task import Task

class TaskManager:
    _instance = None

    def __new__(cls, db_name="tasks.db"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db = Database(db_name)
        return cls._instance

    def add_task(self, task: Task):
        cursor = self.db.execute(
            "INSERT INTO tasks (title, description, category, priority, reminder, completed) VALUES (?, ?, ?, ?, ?, ?)",
            (task.title, task.description, task.category, task.priority, task.reminder, int(task.completed))
        )
        task._Task__id = cursor.lastrowid
        return task.id

    def get_task(self, task_id: int) -> Task | None:
        row = self.db.fetchone("SELECT * FROM tasks WHERE id=?", (task_id,))
        if row:
            return Task(
                task_id=row[0],
                title=row[1],
                description=row[2],
                category=row[3],
                priority=row[4],
                reminder=row[5],
                completed=bool(row[6])
            )
        return None

    def update_task(self, task: Task):
        self.db.execute(
            "UPDATE tasks SET title=?, description=?, category=?, priority=?, reminder=?, completed=? WHERE id=?",
            (task.title, task.description, task.category, task.priority, task.reminder, int(task.completed), task.id)
        )

    def delete_task(self, task_id: int):
        self.db.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    def list_tasks(self, category: str = None, completed: bool = None) -> list[Task]:
        query = "SELECT * FROM tasks"
        params = ()
        filters = []
        if category:
            filters.append("category=?")
            params += (category,)
        if completed is not None:
            filters.append("completed=?")
            params += (int(completed),)
        if filters:
            query += " WHERE " + " AND ".join(filters)
        query += " ORDER BY priority DESC"
        rows = self.db.fetchall(query, params)
        return [
            Task(
                task_id=row[0],
                title=row[1],
                description=row[2],
                category=row[3],
                priority=row[4],
                reminder=row[5],
                completed=bool(row[6])
            )
            for row in rows
        ]

    def close(self):
        self.db.close()
