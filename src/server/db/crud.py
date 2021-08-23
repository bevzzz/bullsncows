# Third-party libraries
import uuid
import sqlalchemy.orm as orm

# Local libraries
# Schemas are Pydantic models
from src.server import schemas
# Models are SqlAlchemy ORM models
from src.server.db import model


# Readers
def get_game(db: orm.Session, game_id: uuid.UUID):
    return db.query(model.Game).filter(model.Game.id == str(game_id)).first()


def get_games(db: orm.Session, skip: int = 0, limit: int = 10):
    return db.query(model.Game).offset(skip).limit(limit).all()


def get_user(db: orm.Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()


# Creators
def create_game(db: orm.Session, user_id: int, number: str):
    pk = uuid.uuid4()
    db_game = model.Game(
        id=str(pk),
        user_id=user_id,
        number=number
    )
    db.add(db_game).commit()
    db.refresh(db_game)
    return db_game


def create_user(db: orm.Session, user: schemas.NewUser):
    db_user = model.User(**user.dict())
    db.add(db_user).commit()
    db.refresh(db_user)
    return db_user

