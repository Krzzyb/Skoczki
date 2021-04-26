class Position: 

    # Constructor:
    def __init__(self, *args):
      if len(args) == 1:  
        self.initFromString(args[0])
      else:    
        self.initFromCoordiates(args[0], args[1])

    def initFromCoordiates(self, x, y):
        self.x = x
        self.y = y

    def initFromString(self, LN):
      letter = LN[0];
      L = ord(letter)
      number = LN[1];
      self.initFromCoordiates(L - 64, int(number))

    # Method:
    def __str__(self):      
        #return "X={},Y={}".format(self.x, self.y)
        letter = chr(self.x + 64)
        return "{}{}".format(letter,self.y)
    def __eq__(self, obj):
      return self.x == obj.x and self.y == obj.y 

    def getAllKnightMoves(self):
      return [
        Position(self.x+2, self.y+1),
        Position(self.x+1, self.y+2),
        Position(self.x-1, self.y+2),
        Position(self.x-2, self.y+1),
        Position(self.x-2, self.y-1),
        Position(self.x-1, self.y-2),
        Position(self.x+1, self.y-2),
        Position(self.x+2, self.y-1)];

    def isOnBoard(self, boardSize):
      if self.x > boardSize:
        return False
      elif self.y > boardSize:
        return False
      elif self.x < 1:
        return False
      elif self.y < 1:
        return False
      else:
        return True

    def getAllFairMoves(self, boardSize):
      allMoves = self.getAllKnightMoves();
      fairMoves = []
      for x in allMoves:
        if (x.isOnBoard(boardSize)):
          fairMoves.append(x) 
      return fairMoves

    def isOnList(self, movesList):
      for x in movesList:
        if self == x:
          return True
      return False

    def getAllFairNotForbiddenMoves(self, boardSize, forbiddenMoves):
      fairMoves = self.getAllFairMoves(boardSize);
      notForbiddenMoves = []
      for x in fairMoves:
        if (x.isOnList(forbiddenMoves) == False):
          notForbiddenMoves.append(x)
      return notForbiddenMoves

    def isOnlyTwo(self, boardSize, visitedMoves):
      connections = []
      fairMoves = self.getAllFairMoves(boardSize)
      for x in visitedMoves:
        for z in fairMoves:
          if x == z:
            connections.append(z)

      if len(connections) == 2:
        return True
      return False