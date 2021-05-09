from Position import Position

def resultCheck (result, boardSize):
    if len(result) == 0:
        return False
    for move in result:
        if len(move.getAllFairAllowedMoves(boardSize, result)) != 2:
            return False
    return True
            
