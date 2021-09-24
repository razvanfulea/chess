import unittest

from main import Game


class GameTest(unittest.TestCase):

    def test_canCreateGame(self):
        game = Game()
