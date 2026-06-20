from fastapi import FastAPI
import pymysql
import json

app = FastAPI()

# 🔗 Connect to MySQL running inside Docker
def get_connection():
    return pymysql.connect(
        host="mysql-db",        
        user="app_user",
        password="app_pass",
        database="app_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# 🗄️ Create table if not exists
def init_db():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT PRIMARY KEY,
                    data JSON NOT NULL
                )
            """)
        conn.commit()

init_db()


@app.get("/")
def home():
    return {"message": "Hello, FastAPI running inside Docker 🚀!"}


@app.get("/user/{user_id}")
def get_user(user_id: int):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT data FROM users WHERE id=%s", (user_id,))
            row = cursor.fetchone()
            if row is None:
                return {"error": "User not found"}
            return json.loads(row["data"])



@app.post("/user/")
def create_user(user: dict):
    user_id = user.get("id")
    if user_id is None:
        return {"error": "User must have an 'id' field"}

    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (id, data) VALUES (%s, %s)",
                (user_id, json.dumps(user))
            )
        conn.commit()
    return user


@app.get("/users/")
def list_users():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT data FROM users")
            rows = cursor.fetchall()
            return [json.loads(row["data"]) for row in rows]



@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()
        if cursor.rowcount == 0:
            return {"error": "User not found"}
    return {"message": "User deleted"}


@app.put("/user/{user_id}")
def update_user(user_id: int, updated_user: dict):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE users SET data=%s WHERE id=%s",
                (json.dumps(updated_user), user_id)
            )
        conn.commit()
        if cursor.rowcount == 0:
            return {"error": "User not found"}
    return updated_user
