
Pawn = 2
Pawnb = 3
Knight = 4
Knightb = 5
Bishop = 8
Bishopb = 9
Rook = 16
Rookb = 17
Queen = 32
Queenb = 33
King = 64
Kingb = 65

def read_Fen(note, board):
    start = 64
    flip = True
    for piece in note.split("/"):
        note = note[::-1]
        for i, x in enumerate(list(piece)):
            try:
                y = int(x)
                start -= y
            except ValueError:
                start -= 1
                if x == "P":
                    board[start] = Pawn
                elif x == "B":
                    board[start] = Bishop
                elif x == "R":
                    board[start] = Rook
                elif x == "Q":
                    board[start] = Queen
                elif x == "K":
                    board[start] = King
                elif x == "N":
                    board[start] = Knight
                elif x == "p":
                    board[start] = Pawnb
                elif x == "b":
                    board[start] = Bishopb
                elif x == "r":
                    board[start] = Rookb
                elif x == "q":
                    board[start] = Queenb
                elif x == "k":
                    board[start] = Kingb
                elif x == "n":
                    board[start] = Knightb
                elif x == "/":
                    flip = not flip
                else:
                    pass
            
    return board