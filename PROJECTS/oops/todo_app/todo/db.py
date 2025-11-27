import sqlite3
from typing import Optional

class Database:
    def __init__(self, db_name: str = "tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        query_tasks = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            category TEXT,
            priority INTEGER,
            reminder TEXT,   -- ISO date-time string or None
            completed INTEGER DEFAULT 0
        );"""
        self.conn.execute(query_tasks)
        self.conn.commit()

    def execute(self, query: str, params: tuple = ()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor

    def fetchone(self, query: str, params: tuple = ()) -> Optional[tuple]:
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def fetchall(self, query: str, params: tuple = ()) -> list:
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def close(self):
        self.conn.close()
