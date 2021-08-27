# Built-in libraries
import uuid

# Third-party libraries
from pydantic import BaseModel


# Game
class GameBase(BaseModel):
    pass


class NewGame(GameBase):
    user_id: int
    number: str


class Game(GameBase):
    id: uuid.UUID
    user_id: int
    number: str

    class Config:
        orm_mode = True


# User
class UserBase(BaseModel):
    id: int
    username: str


class NewUser(UserBase):
    pass


class User(UserBase):
    pass

    class Config:
        orm_mode = True


