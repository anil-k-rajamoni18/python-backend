```
todo_app/
│
├── todo/
│   ├── __init__.py
│   ├── task.py           # Task class
│   ├── task_manager.py   # Singleton TaskManager with SQLite integration
│   ├── db.py             # DB connection & setup
│   └── cli.py            # CLI interface
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_task.py
│   └── test_task_manager.py
│
├── main.py
└── requirements.txt
```