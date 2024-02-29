import unittest
from pytactoe import Game, createBoard
from utils import playbackGame

class TestGameClass(unittest.TestCase):
    def testInstance(self):
        myGame = Game()
        self.assertTrue(isinstance(myGame, Game), "Game() should create a game instance")
class TestNextMove(unittest.TestCase):
    def testNextMoveExists(self):
        myGame = Game()
        self.assertTrue(hasattr(myGame, 'nextMove') and callable(getattr(myGame, 'nextMove')), 'nextMove should update the board appropriately')
    def testNextMoveExpected(self):
        ScenarioOne = [('x', (0, 0))]
        game = playbackGame(ScenarioOne)
        self.assertEqual(game.getBoard(), [
            ['x', None, None],
            [None, None, None],
            [None, None, None],
        ], 'nextMove should not allow a player to claim an occupied space')
    def testNextMoveSpaceTaken(self):
        game = Game()
        game.nextMove('x', (0, 0))
        message = 'nextMove should not allow a player to claim an occupied space'
        with self.assertRaises(IndexError, msg=message):
            game.nextMove('o', (0, 0))
        self.assertEqual(game.getBoard(), [
            ['x', None, None],
            [None, None, None],
            [None, None, None],
        ], message)
    def testNextMovePlayerTurns(self):
        game = Game()
        game.nextMove('x', (0, 0))
        game.nextMove('x', (0, 1))
        self.assertEqual(game.getBoard(), [
            ['x', None, None],
            [None, None, None],
            [None, None, None],
        ], 'nextMove should not allow a player to play two moves in a row')
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
        self.assertEqual(game.getBoard(), startingBoard, message)
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
        self.assertEqual(game.getBoard(), [
            ['x', 'x', 'x'],
            ['o', 'o', None],
            [None, None, None],
        ], 'Should not allow a player to make a move after the game is over')
    def testGamePlayers(self):
        game = Game()
        game.nextMove('x', (0, 0))
        game.nextMove('o', (0, 1))
        message = "Should only allow player 'x' and 'o' to make moves"
        with self.assertRaises(ValueError, msg=message):
            game.nextMove('0', (0, 2))
        with self.assertRaises(ValueError, msg=message):
            game.nextMove(0, (0, 2))
        self.assertEqual(game.getBoard(), [
            ['x', 'o', None],
            [None, None, None],
            [None, None, None],
        ], message)

class TestIsOver(unittest.TestCase):
    def testFunctionExists(self):
        game = Game()
        self.assertTrue(hasattr(game, 'isOver') and callable(getattr(game, 'isOver')))
    def testFalseIfOver(self):
        ScenarioOne = [
            ('x', (0, 0)),
            ('o', (1, 0)),
            ('x', (0, 1)),
            ('o', (1, 1)),
        ]
        game = playbackGame(ScenarioOne)
        self.assertFalse(game.isOver(), 'isOver() should return false when game is over')
    def testTrueIfOver(self):
        ScenarioOne = [
            ('x', (0, 0)),
            ('o', (1, 0)),
            ('x', (0, 1)),
            ('o', (1, 1)),
            ('x', (0, 2)),
        ]
        game = playbackGame(ScenarioOne)
        self.assertTrue(game.isOver(), 'isOver() should return true when game is over')

class TestGetBoard(unittest.TestCase):
    def testFunctionExists(self):
        game = Game()
        self.assertTrue(hasattr(game, 'getBoard') and callable(getattr(game, 'getBoard')), 'Game should have getBoard function')
    def testBoardShape(self):
        ScenarioOne = [
            ('x', (0, 0)),
            ('o', (1, 0)),
            ('x', (0, 1)),
            ('o', (1, 1)),
        ]
        game = playbackGame(ScenarioOne)
        board = game.getBoard()
        self.assertIsInstance(board, list, 'board() should return a two-dimensional 3x3 array')
        self.assertEqual(len(board), 3, 'board() should return a two-dimensional 3x3 array')
        for row in board:
            self.assertIsInstance(row, list, 'board() should return a two-dimensional 3x3 array')
            self.assertEqual(len(row), 3, 'board() should return a two-dimensional 3x3 array')
    def testBoardContents(self):
        ScenarioOne = [
            ('x', (0, 0)),
            ('o', (1, 0)),
            ('x', (0, 1)),
            ('o', (1, 1)),
        ]
        game = playbackGame(ScenarioOne)
        board = game.getBoard()
        for row in board:
            for value in row:
                self.assertIn(value, ['x', 'o', None], "board should only contain the values 'x', 'o' or null")

class TestPrintBoard(unittest.TestCase):
    def testFunctionExists(self):
        game = Game()
        self.assertTrue(hasattr(game, 'printBoard') and callable(getattr(game, 'printBoard')), 'Game should have printBoard function')
    def testPrintBoardOutput(self):
        # TODO: Investigate how to capture console output for python print statements.
        pass

class TestGameWinner(unittest.TestCase):
    def testFunctionExists(self):
        game = Game()
        self.assertTrue(hasattr(game, 'winner') and callable(getattr(game, 'winner')), 'Game should have winner function')
    def testXWinner(self):
        ScenarioOne = [
            ('x', (0, 0)),
            ('o', (1, 0)),
            ('x', (0, 1)),
            ('o', (1, 1)),
            ('x', (0, 2)),
        ]
        game = playbackGame(ScenarioOne)
        self.assertTrue(game.isOver(), 'isOver should return true when \'x\' wins the game.')
        self.assertEqual(game.winner(), 'x', 'winner should return \'x\' when \'x\' wins the game.')
    def testOWinner(self):
        ScenarioOne = [
            ('o', (0, 0)),
            ('x', (1, 0)),
            ('o', (0, 1)),
            ('x', (1, 1)),
            ('o', (0, 2)),
        ]
        game = playbackGame(ScenarioOne)
        self.assertTrue(game.isOver(), 'isOver should return true when \'o\' wins the game.')
        self.assertEqual(game.winner(), 'o', 'winner should return \'o\' when \'o\' wins the game.')
    def testDraw(self):
        ScenarioOne = [
            ('o', (0, 0)),
            ('x', (1, 0)),
            ('o', (0, 1)),
            ('x', (1, 1)),
            ('o', (1, 2)),
            ('x', (0, 2)),
            ('o', (2, 0)),
            ('x', (2, 1)),
            ('o', (2, 2)),
        ]
        game = playbackGame(ScenarioOne)
        self.assertTrue(game.isOver(), 'isOver should return true when game ends in draw.')
        self.assertEqual(game.winner(), None, 'winner should return None when game is not complete.')
    def testIncompleteGame(self):
        ScenarioOne = [
            ('o', (0, 0)),
            ('x', (1, 0)),
            ('o', (0, 1)),
            ('x', (1, 1)),
            ('o', (1, 2)),
            ('x', (0, 2)),
            ('o', (2, 0)),
            ('x', (2, 1)),
        ]
        game = playbackGame(ScenarioOne)
        self.assertFalse(game.isOver(), 'isOver should return false when game is not complete.')
        self.assertEqual(game.winner(), None, 'winner should return None when game is not complete.')

class TestGameExport(unittest.TestCase):
    def testFunctionExists(self):
        game = Game()
        self.assertTrue(hasattr(game, 'export') and callable(getattr(game, 'export')), 'Game should have export function')
        self.assertIsInstance(game.export(), dict, 'Game export should be a dictionary')
    def testExportDictKeys(self):
        game = Game()
        exDict = game.export()
        self.assertIn('winner', exDict, 'Game export dictionary should have winner key')
        self.assertIn('firstPlayer', exDict, 'Game export dictionary should have firstPlayer key')
        self.assertIn('board', exDict, 'Game export dictionary should have board key')
        self.assertIn('history', exDict, 'Game export dictionary should have history key')
    def testExportDictWinnerX(self):
        ScenarioOne = [
            ('x', (0, 0)),
            ('o', (1, 0)),
            ('x', (0, 1)),
            ('o', (1, 1)),
            ('x', (0, 2)),
        ]
        game = playbackGame(ScenarioOne)
        self.assertEqual(game.export()['winner'], 'x', 'Game export winner should return \'x\' when \'x\' wins the game.')
    def testExportDictWinnerO(self):
        ScenarioOne = [
            ('o', (0, 0)),
            ('x', (1, 0)),
            ('o', (0, 1)),
            ('x', (1, 1)),
            ('o', (0, 2)),
        ]
        game = playbackGame(ScenarioOne)
        self.assertEqual(game.export()['winner'], 'o', 'Game export winner should return \'o\' when \'o\' wins the game.')
    def testExportDictWinnerIncomplete(self):
        ScenarioOne = [
            ('o', (0, 0)),
            ('x', (1, 0)),
            ('o', (0, 1)),
            ('x', (1, 1)),
            ('o', (1, 2)),
            ('x', (0, 2)),
            ('o', (2, 0)),
            ('x', (2, 1)),
        ]
        game = playbackGame(ScenarioOne)
        self.assertEqual(game.export()['winner'], None, 'Game export winner should return None when game is not complete.')
    def testExportDictWinnerDraw(self):
        ScenarioOne = [
            ('o', (0, 0)),
            ('x', (1, 0)),
            ('o', (0, 1)),
            ('x', (1, 1)),
            ('o', (1, 2)),
            ('x', (0, 2)),
            ('o', (2, 0)),
            ('x', (2, 1)),
            ('o', (2, 2)),
        ]
        game = playbackGame(ScenarioOne)
        self.assertEqual(game.export()['winner'], None, 'Game export winner should return None when game is a draw.')
class TestExportFirstPlayer(unittest.TestCase):
    def testX(self):
        ScenarioOne = [('x', (0, 0))]
        game = playbackGame(ScenarioOne)
        self.assertEqual(game.export()['firstPlayer'], 'x', 'Game export firstPlayer entry should be \'x\' if \'x\' makes first move.')
    def testO(self):
        ScenarioOne = [('o', (0, 0))]
        game = playbackGame(ScenarioOne)
        self.assertEqual(game.export()['firstPlayer'], 'o', 'Game export firstPlayer entry should be \'o\' if \'o\' makes first move.')
    def testNone(self):
        ScenarioOne = []
        game = playbackGame(ScenarioOne)
        self.assertEqual(game.export()['firstPlayer'], None, 'Game export firstPlayer entry should be None if neither player has moved yet.')

class TestExportBoard(unittest.TestCase):
    def testBoardShape(self):
        ScenarioOne = [
            ('o', (0, 0)),
            ('x', (1, 0)),
            ('o', (0, 1)),
            ('x', (1, 1)),
        ]
        game = playbackGame(ScenarioOne)
        board = game.export()['board']
        self.assertIsInstance(board, list, 'Game export board field should return list.')
        self.assertEqual(len(board), 3, 'Game export board should have 3 rows.')
        for row in board:
            self.assertIsInstance(row, list, 'Game export board row should be a list.')
            self.assertEqual(len(row), 3, 'Game export board should have 3 columns.')
    def testBoardValues(self):
        ScenarioOne = [
            ('o', (0, 0)),
            ('x', (1, 0)),
            ('o', (0, 1)),
            ('x', (1, 1)),
        ]
        game = playbackGame(ScenarioOne)
        board = game.export()['board']
        for row in board:
            for value in row:
                self.assertIn(value, ('x', 'o', None), 'Game export board should only contain values \'x\', \'o\' or None.')

class TestExportHistory(unittest.TestCase):
    def testHistoryShape(self):
        ScenarioOne = [
            ('x', (0, 0)),
            ('o', (1, 0)),
            ('x', (0, 1)),
            ('o', (1, 1)),
            ('x', (0, 2)),
        ]
        game = playbackGame(ScenarioOne)
        history = game.export()['history']
        self.assertIsInstance(history, list, 'Game export history should be a list.')
        for move in history:
            self.assertIsInstance(move, tuple, 'Moves in exported game history should be tuples.')
            self.assertTrue(len(move), 2)
            player, position = move
            self.assertIn(player, ('x', 'o'))
            self.assertIsInstance(position, tuple, 'Positions should be tuples.')
            self.assertEqual(len(position), 2, 'Positions should have two coordinates.')
            row, col = position
            self.assertIsInstance(row, int, 'Row coordinate should be integer.')
            self.assertIsInstance(col, int, 'Column coordinate should be integer.')
    def testHistoryValues(self):
        ScenarioOne = [
            ('x', (0, 0)),
            ('o', (1, 0)),
            ('x', (0, 1)),
            ('o', (1, 1)),
            ('x', (0, 2)),
        ]
        game = playbackGame(ScenarioOne)
        history = game.export()['history']
        self.assertEqual(len(history), len(ScenarioOne))
        for index, move in enumerate(ScenarioOne):
            player, position = move
            histPlayer, histPosition = history[index]
            self.assertEqual(player, histPlayer, 'Players listed in history should match players that made moves.')
            self.assertTupleEqual(position, histPosition, 'Positions in exported games should match positions of player moves.')

class TestBugRegressions(unittest.TestCase):
    def testBug7(self):
        ScenarioOne = [
            ('x', (0, 1)),
            ('o', (0, 0)),
            ('x', (0, 2)),
            ('o', (1, 0)),
            ('x', (1, 2)),
            ('o', (1, 1)),
            ('x', (2, 0)),
            ('o', (2, 2)),
        ]
        game = playbackGame(ScenarioOne)
        self.assertTrue(game.isOver())
        self.assertEqual(game.winner(), 'o')

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
