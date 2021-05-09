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
      if len(bestResult) < len(result):
        for x in bestResult:
          if (x.isOnlyTwo(boardSize, visitedMoves) == True):
            bestResult = result
             
     
    return bestResult