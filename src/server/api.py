# Third-party libraries
import uuid
import sqlalchemy.orm as orm
from fastapi import FastAPI, Depends
from pydantic import BaseModel

# Local libraries
from src.server.db import crud, model
from src.server import schemas
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


# @app.get("/game/new/{user_id}", response_model=schemas.Game)
@app.get("/game/new/{user_id}")
def new_game(user_id: int, db: orm.Session = Depends(get_db)):
    number = computer.new_number()
    game = schemas.NewGame(
        user_id=user_id,
        number=number
    )
    game = crud.create_game(
        db=db,
        game=game
    )
    game_id = uuid.UUID(game.id)
    return {"id": game_id}
