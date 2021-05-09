from findBestMove import findBestMove
from Position import Position
from result_check import resultCheck

# Arrange
startPoint = Position("D3")
boardSize = 5
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

print("Result check:")
print(resultCheck(moves, boardSize))