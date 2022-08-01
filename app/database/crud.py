from database import Session
from models import User
from schemas import TgUser


def get_user(user_id: int) -> User:
    db = Session()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return user


def get_user_by_address(address: str) -> User:
    db = Session()
    user = db.query(User).filter(User.address == address).first()
    db.close()
    return user


def create_user(user: TgUser) -> User:
    db = Session()
    user = User(id=user.id, address=user.address, redirect_url=user.redirect_url)
    db.add(user)
    db.commit()
    db.close()
    return user


def update_user(user: User) -> User:
    db = Session()
    db.update(user)
    db.commit()
    db.close()
    return user
