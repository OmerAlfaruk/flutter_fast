from fastapi import FastAPI
from routes.user import user as user_router
from config.db import engine, Base
from models.models import UserModel


app = FastAPI(
	title="Fast Flutter API",
	description="A small FastAPI example for learning",
	version="0.1.0",
)

# create DB tables
Base.metadata.create_all(bind=engine)

# include routers so OpenAPI/Swagger shows endpoints
app.include_router(user_router, prefix="", tags=["users"]) 