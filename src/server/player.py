# Build-in libraries
import enum
import random
import typing as t

# Third-party libraries
import uuid


class MODE(int, enum.Enum):
    generate = 1


class Player:

    games: t.Dict[uuid.UUID, str]

    def __init__(self, mode: MODE):
        self.mode = mode
        self.games = {}

    def start_new_game(self) -> uuid.UUID:
        # create a new game
        # @return: id of the new game
        new_id = uuid.uuid4()
        number = self._new_number()
        self.games[new_id] = number
        return new_id

    @staticmethod
    def _new_number():
        nums = random.sample(range(10), 4)
        s = [str(n) for n in nums]
        return "".join(s)

