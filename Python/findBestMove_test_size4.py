from findBestMove import findBestMove
from Position import Position

# Arrange
startPoint = Position("B1")
boardSize = 4
b1SampleResult = [
  Position("B1"),
  Position("D2"),
  Position("B3"),
  Position("D4"),
  Position("C2"),
  Position("B4"),
  Position("D3"),
  Position("B2"),
  Position("A4"),
  Position("C3")
]

# Run
moves = findBestMove(startPoint, startPoint, boardSize, [])

# Assert
print(f"Expected Moves: {[str(move) for move in b1SampleResult]}")
print(f"Returned Moves: {[str(move) for move in moves]}")
