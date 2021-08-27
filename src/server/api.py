# Built-in libraries
from typing import Optional

# Third-party libraries
import uuid
import sqlalchemy.orm as orm
from fastapi import FastAPI, Header, Depends
from pydantic import BaseModel

# Local libraries
import src.server.headers as headers
from src.server import schemas
from src.server.db import crud, model
from src.server.db.db import SessionLocal, engine
from src.server.player import Player, MODE


app = FastAPI()
computer = Player(mode=MODE.generate)

# Inject dependencies
# create the tables (should be done with Alembic)
model.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/game/new/{user_id}")
def new_game(user_id: int, authorization: Optional[str] = Header(None), db: orm.Session = Depends(get_db)):

    if not crud.get_user(db=db, user_id=user_id):
        username, pw = headers.parse_auth(authorization)
        user = schemas.NewUser(id=user_id, username=username)
        crud.create_user(db, user)

    number = computer.new_number()
    game = schemas.NewGame(user_id=user_id, number=number)
    game = crud.create_game(db, game)
    game_id = uuid.UUID(game.id)
    return {"id": game_id}

