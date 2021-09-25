# Build-in libraries
import enum
import random
import typing as t

# Third-party libraries
import uuid

# Local libraries
from server.db import model
from server.app.schemas import Score


class MODE(int, enum.Enum):
    generate = 1


class Player:

    games: t.Dict[uuid.UUID, str]

    def __init__(self, mode: MODE):
        self.mode = mode
        self.games = {}

    @staticmethod
    def new_number():
        nums = random.sample(range(10), 4)
        s = [str(n) for n in nums]
        return "".join(s)

    def get_score(self, game: model.Game, number: str) -> Score:
        score = self._count_matches(game, number)
        if score.bulls == 4:
            score.finished = True
        return score

    @staticmethod
    def _count_matches(game: model.Game, number: str) -> Score:
        target = game.number
        score = Score()
        for n in number:
            if n in target:
                if number.index(n) == target.index(n):
                    # check that the number is in the right position
                    score.bulls += 1
                else:
                    score.cows += 1
        return score
