"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import sys

import isolation
import game_agent
from sample_players import RandomPlayer

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def minimax(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = game_agent.MinimaxPlayer()
        self.game = isolation.Board(self.player1, self.player2)
        self.game.apply_move((2, 3))
        self.game.apply_move((0, 5))
        winner, history, msg = self.game.play()
        print('message:', msg)
        print('winner:', winner == self.player1 and 'player1' or 'player2')
        print(history)
        new_game = isolation.Board(self.player1, self.player2)
        new_game.apply_move((2, 3))
        new_game.apply_move((0, 5))
        print('Init Minimax...')
        print(new_game.to_string())
        for idx, move in enumerate(history):
            print('Minimax Move ', idx + 1)
            new_game = new_game.forecast_move(move)
            print(new_game.to_string())

    def test_alphabeta(self):
        reload(game_agent)
        self.player1 = game_agent.AlphaBetaPlayer()
        self.player2 = game_agent.AlphaBetaPlayer()
        self.game = isolation.Board(self.player1, self.player2)
        self.game.apply_move((4, 1))
        self.game.apply_move((2, 3))
        winner, history, msg = self.game.play()
        print('message:', msg)
        print('winner:', winner == self.player1 and 'player1' or 'player2')
        print(history)
        print(self.game.to_string())
        new_game = isolation.Board(self.player1, self.player2)
        new_game.apply_move((4, 1))
        new_game.apply_move((2, 3))
        print('Init Alphabeta...')
        print(new_game.to_string())
        for idx, move in enumerate(history):
            print('Alphabeta Move ', idx + 1)
            new_game = new_game.forecast_move(move)
            print(new_game.to_string())

if __name__ == '__main__':
    unittest.main()
