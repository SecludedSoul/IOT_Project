from sqlalchemy.orm import Session
from model import User
from schemas import UserSchema

# user by id
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# all user
def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserSchema):
    db_user = User(
        id=user.id,
        name=user.name,
        phone=user.phone,
        address=user.address,
        email=user.email,
        image_url=user.image_url,
        description=user.description
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_data: UserSchema):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        if user_data.name is not None:
            db_user.name = user_data.name
        if user_data.phone is not None:
            db_user.phone = user_data.phone
        if user_data.address is not None:
            db_user.address = user_data.address
        if user_data.email is not None:
            db_user.email = user_data.email
        if user_data.image_url is not None:
            db_user.image_url = user_data.image_url
        if user_data.description is not None:
            db_user.description = user_data.description
        
        db.commit()
        db.refresh(db_user)

        # Use `UserSchema` to serialize the updated user
        return UserSchema.from_orm(db_user)
    return None


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"message": "User deleted"}
    return {"error": "User not found"}
