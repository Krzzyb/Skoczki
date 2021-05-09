from findBestMove import findBestMove, resultCheck
from Position import Position


#Tutaj można zmienić punkt startowy
startPoint = Position("B1")
# a tu wielkosc szachownicy
boardSize = 5 

 
moves = findBestMove(startPoint, startPoint, boardSize, [])
print(f"Result len:{len(moves)} check:{resultCheck(moves, boardSize)}")
print(f"{[str(move) for move in moves]}")
