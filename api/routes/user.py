from fastapi import APIRouter

from api.schemas.user import userBaseSchema
from api.models.models import UserModel
from api.config.db import database

user = APIRouter()
@user.post("/users/")
async def create_user(user: userBaseSchema):
    query = UserModel.insert().values(
        username=user.username,
        email=user.email,
        password=user.password
    )
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}