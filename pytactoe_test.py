import unittest
from pytactoe import Game, createBoard, winsByRow, winsByCol, winsByDiag, winningBoards, normalizeBoardForPlayer, isWinningBoard
from grid import Grid, Grid3x3
from utils import playbackGame

# TODO: add more messages for test cases
class TestGameClass(unittest.TestCase):
    def testInstance(self):
        myGame = Game()
        self.assertTrue(isinstance(myGame, Game), "Game() should create a game instance")
class TestNextMove(unittest.TestCase):
    def testNextMoveExists(self):
        myGame = Game()
        self.assertTrue(hasattr(myGame, 'nextMove') and callable(getattr(myGame, 'nextMove')))
    def testNextMoveExpected(self):
        ScenarioOne = [('x', (0, 0))]
        game = playbackGame(ScenarioOne)
        self.assertEqual(game.getBoard().values, [
            ['x', None, None],
            [None, None, None],
            [None, None, None],
        ])
    def testNextMoveSpaceTaken(self):
        game = Game()
        game.nextMove('x', (0, 0))
        with self.assertRaises(IndexError, msg='Should not allow a player to claim an occupied space'):
            game.nextMove('o', (0, 0))
        self.assertEqual(game.getBoard().values, [
            ['x', None, None],
            [None, None, None],
            [None, None, None],
        ])
    def testNextMovePlayerTurns(self):
        game = Game()
        game.nextMove('x', (0, 0))
        game.nextMove('x', (0, 1))
        self.assertEqual(game.getBoard().values, [
            ['x', None, None],
            [None, None, None],
            [None, None, None],
        ])
    def testNextMoveIllegalPositions(self):
        game = Game()
        startingBoard = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        message = 'Should not allow a player to claim an illegal position'
        with self.assertRaises(IndexError, msg=message):
            game.nextMove('x', (-1, -1))
        with self.assertRaises(IndexError, msg=message):
            game.nextMove('x', (3, 3))
        with self.assertRaises(IndexError, msg=message):
            game.nextMove('x', (0, -1))
        with self.assertRaises(IndexError, msg=message):
            game.nextMove('x', (-1, 0))
        with self.assertRaises(TypeError, msg=message):
            game.nextMove('x')
        with self.assertRaises(TypeError, msg=message):
            game.nextMove('x', { 'row': 0, 'col': 0 })
        with self.assertRaises(TypeError, msg=message):
            game.nextMove('x', (None, None))
        with self.assertRaises(TypeError, msg=message):
            game.nextMove('x', ('0', '0'))
        with self.assertRaises(ValueError, msg=message):
            game.nextMove('x', ())
        self.assertEqual(game.getBoard().values, startingBoard)
    def testGameOver(self):
        ScenarioOne = [
            ('x', (0, 0)),
            ('o', (1, 0)),
            ('x', (0, 1)),
            ('o', (1, 1)),
            ('x', (0, 2)),
        ]
        game = playbackGame(ScenarioOne)
        game.nextMove('o', (1, 2))
        self.assertEqual(game.getBoard().values, [
            ['x', 'x', 'x'],
            ['o', 'o', None],
            [None, None, None],
        ])
    def testGamePlayers(self):
        game = Game()
        game.nextMove('x', (0, 0))
        game.nextMove('o', (0, 1))
        message = "Should only allow player 'x' and 'o' to make moves"
        with self.assertRaises(ValueError, msg=message):
            game.nextMove('0', (0, 2))
        with self.assertRaises(ValueError, msg=message):
            game.nextMove(0, (0, 2))
        self.assertEqual(game.getBoard().values, [
            ['x', 'o', None],
            [None, None, None],
            [None, None, None],
        ])


class TestGameFunctions(unittest.TestCase):
    def testCreateBoard(self):
        myBoard = createBoard()
        self.assertEqual(myBoard.exportGrid(), [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ])
    def testCreateBoardUnique(self):
        self.assertFalse(createBoard() is createBoard())
