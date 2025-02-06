
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
def read_Fen(fen, board):
    index = 0
    piece_map = {
        "P": Pawn, "B": Bishop, "R": Rook, "Q": Queen, "K": King, "N": Knight,
        "p": Pawnb, "b": Bishopb, "r": Rookb, "q": Queenb, "k": Kingb, "n": Knightb
    }
    
    for row in fen.split("/"):
        for char in row: 
            if char.isdigit():
                index += int(char)#
            else:
                board[index] = piece_map.get(char, 0)
                index += 1
    return board