
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
    return [space + move for move, condition in knight_moves if condition]
    
def king_moves(space):
    king_moves = [
            (-9, space % 8 != 0 and space > 8),
            (-8, space % 8 != 0 and space > 8),
            (-7, space % 8 != 0 and space > 8),
            (1, space % 8 != 7 and space < 56),
            (8, space % 8 != 7 and space < 56),
            (9, space % 8 != 7 and space < 56),
            (-1, space % 8 != 7 and space > 8),
            (7, space % 8 != 0 and space < 56),
            (-7, space % 8 != 0 and space > 8)
    ]
    return [space + move for move, condition in king_moves if condition]

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
    
    straights.append(u)
    straights.append(r)
    straights.append(d)
    straights.append(l)
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
    
    diagonals = [dlu, dru, drd, dld]
    return diagonals
    # print(diagonals)
                
            
                 
def get_pawns(space, moved, color):
    pawn_moves = []
    if color:
        if moved:
            pawn_moves = [space + 8]
        else:
            pawn_moves = [space + 8, space + 16]
    else:
        if moved:
            pawn_moves = [space - 8]
        else:
            pawn_moves = [space - 8, space - 16]
    # print(pawn_moves)
    return pawn_moves
                
                    
def legal_moves(board, moves, colour):
    o = 1 if colour else 0
    for x in moves.values():
        for list_item in x:
            for item in list_item:
                if board[item] % 2 == o:
                    index = list_item.index(item)
                    del_in = index -len(list_item)
                    del list_item[del_in]
    return moves

        
        
                
    
    

def poss_moves(board, piece_board, color):
    moves = {}
    o = 1 if color else 0
    for x in board:
        if board[x] != 0:
            if board[x] % 2 == o:
                if board[x] == 2+o:
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
                elif board[x] == 4+o:
                    moves[x] = king_moves(x)
                elif board[x] == 8+o:
                    moves[x] = get_diagonals(x)
                elif board[x] == 16+o:
                    moves[x] = get_straights(x)
                elif board[x] == 32+o:
                    moves[x] = get_straights(x), get_diagonals(x)
                elif board[x] == 64+o:
                    moves[x] = king_moves(x)
    legal = legal_moves(board, moves, color)
    return legal
    

                           
                        
# print(get_diagonals(57))                 
            
