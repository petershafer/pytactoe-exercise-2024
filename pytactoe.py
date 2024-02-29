from grid import Grid3x3

def createBoard():
    return Grid3x3()

def winsByRow():
    grids = [createBoard(), createBoard(), createBoard()]
    for i in range(len(grids)):
        grids[i].setRow(i, [True, True, True])
    return grids

def winsByCol():
    grids = [createBoard(), createBoard(), createBoard()]
    for i in range(len(grids)):
        grids[i].setColumn(i, [True, True, True])
    return grids

def winsByDiag():
    tlbr = createBoard()
    def winsA(value, position):
        i, j = position
        if i == j:
            return True
    tlbr.map(winsA)
    trbl = createBoard()
    def winsB(value, position):
        i, j = position
        if 3 - i - 1 == j:
            return True
    trbl.map(winsB)
    return [tlbr, trbl]

def winningBoards():
    boards = []
    boards.extend(winsByRow())
    boards.extend(winsByCol())
    boards.extend(winsByDiag())
    return boards

def normalizeBoardForPlayer(board, player):
    normalizedBoard = createBoard()
    def normalize(value, position):
        if value == player:
            normalizedBoard.setPosition(position, True)
        else:
            normalizedBoard.setPosition(position, None)
    board.forEach(normalize)
    return normalizedBoard

def isWinningBoard(gameBoard, player):
    winBoards = winningBoards()
    winning = False
    normalizedGameBoard = normalizeBoardForPlayer(gameBoard, player)
    for i in range(len(winBoards)):
        if normalizedGameBoard.contains(winBoards[i]):
            winning = True
    return winning

class Game:
    def __init__(self):
        self.board = createBoard()
        self.gameOver = False
        self.lastPlayer = None
        self.firstPlayer = None
        self.gameWinner = None
        self.history = []
    def nextMove(self, player, position):
        if self.gameOver:
            print('The game is over!')
            return
        if player != 'x' and player != 'o':
            raise ValueError('Invalid player')
        if player == self.lastPlayer:
            print(f'{player} already went. Please wait.')
            return
        if self.board.getPosition(position) != None:
            raise IndexError('Position occupied.')
        self.board.setPosition(position, player)
        self.history.append((player, position))
        self.lastPlayer = player
        self.firstPlayer = player if self.firstPlayer == None else self.firstPlayer
        result = isWinningBoard(self.board, player)
        if result != False:
            self.gameWinner = player
            self.gameOver = True
        if len(self.history) == 9:
            self.gameOver = True
        return
    def isOver(self):
        return self.gameOver
    def getBoard(self):
        return self.board.exportGrid()
    def printBoard(self):
        rows = self.board.getRows()
        for row in rows:
            print(f"{row[0] if row[0] != None else '-'} {row[1] if row[1] != None else '-'} {row[2] if row[2] != None else '-'}")
        return
    def winner(self):
        return self.gameWinner
    def export(self):
        return {
            'winner': self.winner(),
            'firstPlayer': self.firstPlayer,
            'board': self.getBoard(),
            'history': self.history,
        }

# print(winningBoards())

# print(normalizeBoardForPlayer([
#     ['x','o','x'],
#     ['o','x','o'],
#     ['x',None,None],
# ], 'x'))

# print(isWinningBoard([
#     ['x','o','x'],
#     ['o','x','o'],
#     ['x',None,None],
# ], 'x'))






