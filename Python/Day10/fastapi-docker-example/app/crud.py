from sqlalchemy.orm import Session
from app.models import User

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, user):
    db_user = User(id=user.id, data=user.data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user

def update_user(db: Session, user_id: int, data):
    user = get_user(db, user_id)
    if not user:
        return None
    user.data = data
    db.commit()
    db.refresh(user)
    return user
