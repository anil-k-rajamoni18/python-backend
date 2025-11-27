class Task:
    def __init__(self, title: str, description: str = "", category: str = "", priority: int = 0, reminder: str = None, completed: bool = False, task_id: int = None):
        self.__id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.reminder = reminder
        self.completed = completed

    @property
    def id(self):
        return self.__id

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{self.id}] {self.title} ({self.category}) - Priority: {self.priority} - Status: {status}"
