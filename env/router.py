from fastapi import APIRouter, Depends, HTTPException, Path
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import UserSchema, ResponseUser, RequestUser
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create(user: RequestUser, db: Session = Depends(get_db)):
    crud.create_user(db, user=user.parameter)
    return ResponseUser(code=200, message="User created", status="ok").dict(exclude_none=True)

@router.get("/")
async def get(db: Session = Depends(get_db)):
    _users = crud.get_user(db, 0, 100)
    return ResponseUser(code=200, message="User All", status="ok", result=_users).dict(exclude_none=True)

@router.get("/{id}")
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    _user = crud.get_user_by_id(db, id)
    if _user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return ResponseUser(code=200, message="User Here", status="ok", result=_user).dict(exclude_none=True)

@router.patch("/update")
async def update_user(user: RequestUser, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id=user.parameter.id, user_data=user.parameter)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return ResponseUser(code=200, message="User Updated Leaw!", status="ok", result=updated_user)

@router.delete("/delete/{id}")
async def delete_user(id: int, db: Session = Depends(get_db)):
    result = crud.delete_user(db, user_id=id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return ResponseUser(code=200, message="User Deleted", status="ok").dict(exclude_none=True)
