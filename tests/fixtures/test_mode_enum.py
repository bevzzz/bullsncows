import unittest
from src.server.player import MODE


class TestModeEnum(unittest.TestCase):
    """
    `Player` has several modes defined in a dedicated enum
    Test that the assigned values are not confused
    """

    @classmethod
    def setUpClass(cls):
        cls.enum = MODE

    def test_enums_are_correct(self):
        self.assertEqual(self.enum.generate, 1)
