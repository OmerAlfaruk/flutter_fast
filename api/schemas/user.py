from pydantic import BaseModel


class userBaseSchema(BaseModel):
    username: str
    email: str
    password: str

