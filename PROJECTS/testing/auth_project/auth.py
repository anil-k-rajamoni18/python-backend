import sqlite3
import hashlib

class SQLiteAuthService:
    def __init__(self, db_path="users.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL
                )
            """)

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username: str, password: str):
        if len(password) < 6:
            raise ValueError("Password too short")

        hashed = self._hash_password(password)
        try:
            with self.conn:
                self.conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        except sqlite3.IntegrityError:
            raise ValueError("Username already exists")
        return True

    def login(self, username: str, password: str) -> bool:
        hashed = self._hash_password(password)
        cursor = self.conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed))
        return cursor.fetchone() is not None

    def is_registered(self, username: str) -> bool:
        cursor = self.conn.execute("SELECT 1 FROM users WHERE username=?", (username,))
        return cursor.fetchone() is not None
