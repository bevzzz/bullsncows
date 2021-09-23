# Built-in libraries
from typing import Optional

# Third-party libraries
import uuid
import sqlalchemy.orm as orm
from fastapi import FastAPI, Header, Body, Depends, status, HTTPException

# Local libraries
import src.server.app.headers as headers
from src.server.app import schemas
from src.server.db import crud, model
from src.server.db.db import engine, start_new_db_session
from src.server.player import Player, MODE


# Inject dependencies
# create the tables (should be done with Alembic)
model.Base.metadata.create_all(bind=engine)

app = FastAPI()
computer = Player(mode=MODE.generate)


@app.post("/game/new/{user_id}", status_code=status.HTTP_201_CREATED)
def new_game(
        user_id: int,
        authorization: Optional[str] = Header(None),
        db: orm.Session = Depends(start_new_db_session)
):
    """
    Start a new game
    :param user_id: internal user ID
    :param authorization: user credentials (for a new entry in the database)
    :param db: database session
    :return: an ID of the game
    """

    if not crud.get_user(db=db, user_id=user_id):
        username, pw = headers.parse_auth(authorization)
        user = schemas.NewUser(id=user_id, username=username)
        crud.create_user(db, user)

    number = computer.new_number()
    game = schemas.NewGame(user_id=user_id, number=number)
    game = crud.create_game(db, game)
    game_id = uuid.UUID(game.id)
    return {"id": game_id}


@app.get("/game/guess/{game_id}", response_model=schemas.Score, status_code=status.HTTP_200_OK)
def get_score(
        game_id: uuid.UUID,
        number: str = Body(..., embed=True),
        db: orm.Session = Depends(start_new_db_session)
):
    """
    Make a guess at the number
    :param game_id: the game being played
    :param number: user's guess
    :param db: database session
    :return: bulls and cows count and the game's status (active or not)
    """

    game = crud.get_game(db, game_id)
    if not game.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The game is no longer active"
        )

    score = computer.get_score(game, number)
    if score.finished:
        game.is_active = False
        crud.update_status(db, game.id, game)
    return score
