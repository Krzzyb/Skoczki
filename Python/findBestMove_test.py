from findBestMove import findBestMove
from Position import Position

#Tutaj można zmienić punkt startowy
startPoint = Position("C3")
# a tu wielkosc szachownicy
boardSize = 7 

 
moves = findBestMove(startPoint, startPoint, boardSize, [])
print(f"Result:{len(moves)}")
print(f"{[str(move) for move in moves]}")