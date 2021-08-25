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

    @staticmethod
    def new_number():
        nums = random.sample(range(10), 4)
        s = [str(n) for n in nums]
        return "".join(s)

