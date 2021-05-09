def resultCheck (result, boardSize):
    if len(result) == 0:
        return False
    for move in result:
        if len(move.getAllFairAllowedMoves(boardSize, result)) != 2:
            return False
    return True

def findBestMove(currentPosition, startPoint, boardSize, visitedMoves):
    moves = currentPosition.getAllFairMoves(boardSize); 
    newVisitedMoves = visitedMoves[:]
    newVisitedMoves.append(currentPosition)
    if len(moves) == 0:
      return []   
    matches = [item for item in moves if item in visitedMoves]
    if len(matches) == 2:
      return newVisitedMoves

    if len(matches) > 2:
      return []    
   
    bestResult = []
    moves = currentPosition.getAllFairNotForbiddenMoves(boardSize, visitedMoves); 
    for nextMove in moves:
      result = findBestMove(nextMove,startPoint, boardSize, newVisitedMoves)
      if len(bestResult) < len(result) and resultCheck(result, boardSize):
        bestResult = result;     
     
    return bestResult
