import sqlite3
from typing import Optional

class Database:
    def __init__(self, db_name: str = "students.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        query_students = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            type TEXT NOT NULL,  -- 'undergrad' or 'postgrad'
            year INTEGER,        -- for undergrad
            thesis TEXT          -- for postgrad
        );"""
        query_courses = """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_name TEXT NOT NULL,
            grade TEXT NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(id)
        );"""
        self.conn.execute(query_students)
        self.conn.execute(query_courses)
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
