# Third-party libraries
import uuid
from fastapi import FastAPI
from pydantic import BaseModel

# Local libraries
from src.server.player import Player, MODE


app = FastAPI()
computer = Player(mode=MODE.generate)


# Models
class NewGame(BaseModel):
    id: uuid.UUID


@app.get("/game/new", response_model=NewGame)
def new_game():
    game_id = computer.start_new_game()
    return {"id": game_id}
