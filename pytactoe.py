def createBoard():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def setRow(grid, row, value):
    for i in range(len(grid)):
        if i == row:
            for j in range(len(grid[i])):
                grid[i][j] = value

def winsByRow():
    grids = [createBoard(), createBoard(), createBoard()]
    for i in range(len(grids)):
        setRow(grids[i], i, True)
    return grids

def setCol(grid, col, value):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j == col:
                grid[i][j] = value

def winsByCol():
    grids = [createBoard(), createBoard(), createBoard()]
    for i in range(len(grids)):
        setCol(grids[i], i, True)
    return grids

def winsByDiag():
    tlbr = createBoard()
    for i in range(len(tlbr)):
        for j in range(len(tlbr[i])):
            if i == j:
                tlbr[i][j] = True
    trbl = createBoard()
    for i in range(len(trbl)):
        for j in range(len(trbl[i])):
            if len(trbl) - i - 1 == j:
                trbl[i][j] = True
    return [tlbr, trbl]

def winningBoards():
    boards = []
    boards.extend(winsByRow())
    boards.extend(winsByCol())
    boards.extend(winsByDiag())
    return boards

def normalizeBoardForPlayer(board, player):
    normalizedBoard = createBoard()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                normalizedBoard[i][j] = True
            else:
                normalizedBoard[i][j] = None
    return normalizedBoard

def matchingBoard(gameBoard, patternBoard):
    contains = True
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[i])):
            if patternBoard[i][j] == True and gameBoard[i][j] == None:
                contains = False
    return contains

def isWinningBoard(gameBoard, player):
    winBoards = winningBoards()
    winning = False
    normalizedGameBoard = normalizeBoardForPlayer(gameBoard, player)
    for i in range(len(winBoards)):
        if matchingBoard(normalizedGameBoard, winBoards[i]):
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
        if player == self.lastPlayer:
            print(f'{player} already went. Please wait.')
            return
        self.board[position[0]][position[1]] = player
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
        return self.board
    def printBoard(self):
        for row in self.board:
            print(f"{row[0] if row[0] != None else '-'} {row[1] if row[1] != None else '-'} {row[2] if row[2] != None else '-'}")
        return
    def winner(self):
        return self.gameWinner
    def export(self):
        return {
            'winner': self.winner,
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






