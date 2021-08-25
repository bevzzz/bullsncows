# Third-party libraries
import sqlalchemy.orm as orm
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey

from src.server.db.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)

    games = orm.relationship("Game", back_populates="user")


class Game(Base):
    __tablename__ = "game"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), index=True)
    number = Column(String)
    is_active = Column(Boolean, default=True)

    user = orm.relationship("User", back_populates="games")

