import json

import pymysql
from fastapi import FastAPI, HTTPException

app = FastAPI()


def get_connection():
    """Create and return a MySQL database connection."""
    return pymysql.connect(
        host="mysql-db",
        user="app_user",
        password="app_pass",
        database="app_db",
        cursorclass=pymysql.cursors.DictCursor,
    )


def init_db():
    """Initialize the database and create tables if they do not exist."""
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INT PRIMARY KEY,
                    data JSON NOT NULL
                )
                """
            )
        conn.commit()


@app.on_event("startup")
def startup_event():
    """Run database initialization on application startup."""
    init_db()


@app.get("/")
def home():
    """Health check endpoint."""
    return {"message": "Hello, FastAPI running inside Docker 🚀!"}


@app.get("/user/{user_id}")
def get_user(user_id: int):
    """Fetch a user by ID."""
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT data FROM users WHERE id = %s",
                (user_id,),
            )
            row = cursor.fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="User not found")

    return json.loads(row["data"])


@app.post("/user/")
def create_user(user: dict):
    """Create a new user."""
    user_id = user.get("id")
    if user_id is None:
        raise HTTPException(
            status_code=400,
            detail="User must have an 'id' field",
        )

    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (id, data) VALUES (%s, %s)",
                (user_id, json.dumps(user)),
            )
        conn.commit()

    return user


@app.get("/users/")
def list_users():
    """List all users."""
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT data FROM users")
            rows = cursor.fetchall()

    return [json.loads(row["data"]) for row in rows]


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    """Delete a user by ID."""
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM users WHERE id = %s",
                (user_id,),
            )
            affected_rows = cursor.rowcount
        conn.commit()

    if affected_rows == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted"}


@app.put("/user/{user_id}")
def update_user(user_id: int, updated_user: dict):
    """Update an existing user."""
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE users SET data = %s WHERE id = %s",
                (json.dumps(updated_user), user_id),
            )
            affected_rows = cursor.rowcount
        conn.commit()

    if affected_rows == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user
