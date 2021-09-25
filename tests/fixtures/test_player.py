import unittest
import uuid

# Local libraries
from server.db.model import Game
from server.player import MODE, Player
from server.app.schemas import Score


class TestModeEnum(unittest.TestCase):
    """
    `Player` should be able to create the number
    and score how successful a user's guess was against it
    """

    game = Game(
        id=uuid.UUID("fe015306-4c10-4bff-91eb-28f3196e1550"),
        user_id=2071,
        number='2375',
        is_active=True
    )

    def setUp(self) -> None:
        self.player = Player(MODE.generate)

    def test_player_instantiated(self) -> None:
        """
        Tests that `self.player` was instantiated
        """
        self.assertIsInstance(self.player, Player)

    def test_generates_number(self) -> None:
        """
        Tests that `Player` generates a 4-digit number and coverts it to a string
        """
        # arrange/act
        num = self.player.new_number()
        # assert
        self.assertEqual(len(num), 4)
        self.assertIsInstance(num, str)

    def test_count_matches(self) -> None:
        """
        Tests that `_count_matches()` method gives the right count
        """
        # arrange
        guess = '7942'
        want = Score(bulls=0, cows=2, finished=False)
        # act
        got: Score = self.player._count_matches(self.game, guess)
        # assert
        self.assertEqual(want, got)

    def test_4_bulls_end_the_game(self):
        """
        Test that if all 4 numbers are guessed correctly, `get_score()` marks it as finished
        """
        # arrange
        guess = '2375'
        want = Score(bulls=4, cows=0, finished=True)
        # act
        got: Score = self.player.get_score(self.game, guess)
        # assert
        self.assertEqual(want, got)
