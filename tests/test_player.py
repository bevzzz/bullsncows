import unittest
from src.server.player import MODE, Player


class TestModeEnum(unittest.TestCase):
    """
    `Player` should be able to create the number
    and score how successful a user's guess was against it
    """

    @classmethod
    def setUp(cls):
        cls.player = Player(MODE.generate)

    def test_player_instantiated(self):
        self.assertIsInstance(self.player, Player)

    def test_generates_number(self):
        # arrange/act
        num = self.player.new_number()
        # assert
        self.assertEqual(len(num), 4)
        self.assertIsInstance(num, str)

