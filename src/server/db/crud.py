# Third-party libraries
import uuid
import sqlalchemy.orm as orm
from typing import List, Dict
from pydantic import BaseModel

# Local libraries
# Schemas are Pydantic models
from src.server.app import schemas
# Models are SqlAlchemy ORM models
from src.server.db import model


def add_commit_refresh(db: orm.Session, data: BaseModel):
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


# Readers
def get_game(db: orm.Session, game_id: uuid.UUID) -> model.Game:
    return db.query(model.Game).filter(model.Game.id == str(game_id)).first()


def get_games(db: orm.Session, skip: int = 0, limit: int = 10) -> List[model.Game]:
    return db.query(model.Game).offset(skip).limit(limit).all()


def get_user(db: orm.Session, user_id: int) -> model.User:
    return db.query(model.User).filter(model.User.id == user_id).first()


# Creators
def create_game(db: orm.Session, game: schemas.NewGame):
    pk = uuid.uuid4()
    db_game = model.Game(id=str(pk), **game.dict())
    return add_commit_refresh(db, db_game)


def create_user(db: orm.Session, user: schemas.NewUser):
    db_user = model.User(**user.dict())
    return add_commit_refresh(db, db_user)


# Updaters
def update_game(db: orm.Session, game_id: uuid.UUID, upd: Dict):
    db.query(model.Game).filter(model.Game.id == game_id).update(upd)
    db.commit()
    return None


def update_status(db: orm.Session, game_id: uuid.UUID, game: model.Game):
    return update_game(db, game_id, {model.Game.is_active: game.is_active})

