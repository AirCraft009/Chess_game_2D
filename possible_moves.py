
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

straight_sliding = [Rook, Rookb, Queen, Queenb]
diagonal_sliding = [Bishop, Bishopb, Queen, Queenb]

offsets = {
    "up": 8,
    "down": -8,
    "left": -1,
    "right": 1,
    "dia_r_up": 9,
    "dia_r_down": -7,
    "dia_l_up": 7,
    "dia_l_down": -9
}

left_edge = [0, 8, 16, 24, 32, 40, 48, 56]
bootom = [0, 1, 2, 3, 4, 5, 6, 7]
distance_top = {}
distance_left = {}
distance_right = {}
distance_bottom = {}


white_pieces = {}
black_pieces = {}
for x in range(64):
    distance_left[x] = x % 8
    distance_right[x] = 7 - (x % 8)
    for i in left_edge:
        if x >= i and x < i + 8:
            distance_bottom[x] = i//8
    distance_top[x] = 7 - distance_bottom[x]


def knight_moves(space):
    knight_moves = [
            (-17, space % 8 != 0 and space > 16),
            (-15, space % 8 != 7 and space > 16),
            (-10, space % 8 > 1 and space > 8),
            (-6, space % 8 < 6 and space > 8),
            (6, space % 8 > 1 and space < 56),
            (10, space % 8 < 6 and space < 56),
            (15, space % 8 != 0 and space < 48),
            (17, space % 8 != 7 and space < 48)
        ]
    l1 = [space + move for move, condition in knight_moves if condition]
    l2 = [[item] for item in l1]
    return l2
    
def king_moves(space):
    king_moves = [
            (-9, space % 8 != 0 and space > 8),
            (-8, space % 8 != 0 and space > 8),
            (-7, space % 8 != 0 and space > 8),
            (-1, space % 8 != 7 and space > 0),
            (8, space % 8 != 7 and space < 56),
            (9, space % 8 != 7 and space < 56),
            (7, space % 8 != 0 and space < 56),
            (1, space % 8 != 0 and space < 63)
    ]
    
    l1 = [space + move for move, condition in king_moves if condition]
    # print(l1)
    l2 = [[item] for item in l1]
    return l2

def get_straights(space):
    u = []
    r = []
    d = []
    l = []
    straights = []
    for x in range(4):
        for y in range(1, 9):
            if x == 0:
                up = (space + offsets["up"]*y)
                if up <= 56:
                    u.append(up)
            elif x == 1:
                right = (space + offsets["right"]*y)
                if right%8 <= 7 and right // 8 == space // 8:
                    r.append(right)
            elif x == 2:
                down = (space + offsets["down"]*y)
                if down >= 0:
                    d.append(down)
            else:
                left = (space + offsets["left"]*y)
                if left%8 >= 0 and left // 8 == space // 8:
                    l.append(left)
    
    straights = [u, r, d, l]
    return straights

def get_diagonals(space):
    dl = distance_left[space]
    dr = distance_right[space]
    dru = []
    drd = []
    dlu = []
    dld = []
    for x in range(4):
        if x == 0:
            for y in range(1,dl+1):
                lu = space + offsets["dia_l_up"]*y
                if lu <= 63:
                    dlu.append(lu)
        elif x == 1:
            for y in range(1, dr+1):
                ru = space + offsets["dia_r_up"]*y
                if ru <= 63:
                    dru.append(ru)      
        elif x == 2:
            for y in range(1, dr+1):
                rd = space + offsets["dia_r_down"]*y
                if rd >= 0:
                    drd.append(rd)
        else:
            for y in range(1, dl+1):
                ld = space + offsets["dia_l_down"]*y
                if ld >= 0:
                    dld.append(ld)
    
    diagonals = [dld, dlu, drd, dru]
    return diagonals
    # print(diagonals)
                
            
                 
def get_pawns(space, moved, color):
    pawn_moves = []
    if color:
        if moved:
            pawn_moves = [space + 8 if space < 56 else 0]
        else:
            pawn_moves = [space + 8 if space < 56 else 0, space + 16 if space < 48 else 0]
    else:
        if moved:
            pawn_moves = [space - 8 if space > 7 else 0]
        else:
            pawn_moves = [space - 8 if space > 7 else 0, space - 16 if space > 15 else 0]
    # print(pawn_moves)
    l2 = [[item] for item in pawn_moves]
    return l2
                
        
   
   
   
def legal_move(pseudo_moves, board, color):
    legal_moves= {}
    moves = []
    o = 0 if color else 1
    for origin_space in pseudo_moves:
        moves.clear()
        """        
        if board[origin_space] == 2+o:# or board[origin_space] == 4+o or board[origin_space] == 64+o:
            for space in pseudo_moves[origin_space]:
                if board[space] % 2 == o:
                    continue
                else:
                    moves.append(space)
            legal_moves[origin_space] = moves
            """
        for poss_spaces in pseudo_moves[origin_space]:
            for space in poss_spaces:
                if board[space] == 0:
                    moves.append(space)
                elif board[space] % 2 == o:
                    break
                else:
                    moves.append(space)
                    break
        legal_moves[origin_space] = [item for item in moves]
    return legal_moves
                    
             
                
    
    

def poss_moves(board, piece_board, color):
    moves = {}
    o = 0 if color else 1
    for x in board:
        if board[x] != 0:
            if board[x] % 2 == o:
                if board[x] == 2+o:
                    """                    
                    smove = get_pawns(x, piece_board[x].moved, color)
                    for m in smove:
                        if board[m]%2 == o:
                            smove.remove(m)
                            break
                        if board[m] == 0:
                            pass
                        else:
                            smove = smove[:smove.index(m):smove.index(m)+1]
                            break
                        moves[x] = smove
                        """
                    moves[x] = get_pawns(x, piece_board[x].moved, color)
                elif board[x] == 4+o:
                    moves[x] = knight_moves(x)
                elif board[x] == 8+o:
                    moves[x] = get_diagonals(x)
                elif board[x] == 16+o:
                    moves[x] = get_straights(x)
                elif board[x] == 32+o:
                    moves[x] = get_straights(x)  +  get_diagonals(x)
                elif board[x] == 64+o:
                    moves[x] = king_moves(x)
    legal = legal_move(moves, board, color)
    return legal
    

                           
if __name__ == "__main__":                        
    # print(get_diagonals(57))         
    # print(get_straights(57))        
    # print(get_pawns(57, False, False))
    print(king_moves(28))
    # print(knight_moves(1))
