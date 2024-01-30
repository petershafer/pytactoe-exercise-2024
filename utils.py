from pytactoe import Game

verbose = True

def playbackGame(moveHistory):
    game = Game()
    if verbose:
        print("Let's play a game.")
    for move in moveHistory:
        if game.isOver():
            break
        if verbose:
            print(f"{move[0]} chooses position {move[1]}")
        game.nextMove(move[0], move[1])
        if game.isOver():
            if verbose:
                game.printBoard()
            if game.winner() == None:
                if verbose:
                    print("It's a draw game!")
                return game
            else:
                if verbose:
                    print(f"{game.winner()} has won the game!")
    return game

scenarioOne = [
    ('o', (0, 0)),
    ('x', (1, 0)),
    ('o', (0, 1)),
    ('x', (1, 1)),
    # ('o', (1, 2)),
    ('o', (0, 2)),
    ('x', (0, 2)),
    ('o', (2, 0)),
    ('x', (2, 1)),
    ('o', (2, 2)),
]
game = playbackGame(scenarioOne);