from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app import crud, schemas

app = FastAPI(title="FastAPI + MySQL (ORM)")

# Create tables on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "FastAPI + SQLAlchemy + MySQL 🚀"}

@app.post("/user/", response_model=schemas.UserResponse)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing = crud.get_user(db, user.id)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db, user)

@app.get("/user/{user_id}", response_model=schemas.UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/", response_model=list[schemas.UserResponse])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.put("/user/{user_id}", response_model=schemas.UserResponse)
def update_user(
    user_id: int,
    updated_data: dict,
    db: Session = Depends(get_db)
):
    user = crud.update_user(db, user_id, updated_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/user/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
