from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.user import userBaseSchema
from models.models import UserModel
from config.db import get_db

user = APIRouter()


@user.post("/users/")
def create_user(user: userBaseSchema, db: Session = Depends(get_db)):
    db_user = UserModel(username=user.username, email=user.email, password=user.password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "username": db_user.username, "email": db_user.email}


@user.get("auth/login")
def login(user:userBaseSchema,db:Session=Depends(get_db)):
    db_user=db.query(UserModel).filter(UserModel.email==user.email)

    isMatch=user.password==db_user.email

    if not isMatch:
        raise Exception("Incorrect Password")
    
    return db_user


    
 

