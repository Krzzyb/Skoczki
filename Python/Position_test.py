from Position import Position

# constructor tests
p1 = Position("D3")

# to string test
print(f"p1=", p1)

# test getAllFairMoves
moves = p1.getAllFairMoves(3)
print(f"getallFairMoves({p1})")
print(f"{[str(move) for move in moves]}")


# test isOnlyTwo
visitedMoves = [Position("B2")]
result = p1.isOnlyTwo(3, visitedMoves)
print(f"D3.isOnlyTwo([B2])={result}")

visitedMoves = [Position("B2"),Position("C1")]
result = p1.isOnlyTwo(3, visitedMoves)
print(f"D3.isOnlyTwo([B2,C1])={result}")