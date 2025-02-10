import random
import time
import pygame
from fen_read import read_Fen
from possible_moves import poss_moves, first_poss_depth_first
from piece_board import piece_board, Piece

points_black = 0
points_white = 0




while True:
    color = input("what color do you want to play as? (white or black)")  
    match color:
        case "white":
            c = True
            break
        case "black":
            c = False
            break
        case _:
            print("invalid input")
            continue
        
board = {}
for x in range(64):
    board[x] = 0
        
while True:
    fen = input("do you want the basic starting position? (y/n)")
    if fen == "n":       
        position = input("what position do you want to start at? (fen)")
        try:
            board = read_Fen(position, board)
            break
        except:
            print("invalid fen")
    elif fen == "y":
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQBNR"
        board = read_Fen(fen, board) if c else read_Fen(fen, board)  
        # print(board)
        break
    else:
        print("invalid input")
        continue
        
        
#initialize screen and clock
screen = pygame.display.set_mode((800 , 800))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
pygame.init()
pos_board = {}
board_pieces = {}

images = [
    white_Pawn = pygame.image.load('white_pawn.png').convert_alpha(),
    black_Pawn = pygame.image.load('black_pawn.png').convert_alpha(),
    white_Knight = pygame.image.load('white_knight.png').convert_alpha(),
    black_Knight = pygame.image.load('black_knight.png').convert_alpha(),
    white_Bishop = pygame.image.load('white_bishop.png').convert_alpha(),
    black_Bishop = pygame.image.load('black_bishop.png').convert_alpha(),
    white_Rook = pygame.image.load('white_rook.png').convert_alpha(),
    black_Rook = pygame.image.load('black_rook.png').convert_alpha(),
    white_Queen = pygame.image.load('white_queen.png').convert_alpha(),
    black_Queen = pygame.image.load('black_queen.png').convert_alpha(),
    white_King = pygame.image.load('white_king.png').convert_alpha(),
    black_King = pygame.image.load('black_king.png').convert_alpha()
    ]

    
def draw_board():
    """
    draw the board
    depending on if you start as white or black
    the first square will be black or white
    """
    if c:
        for x in range(8):
            for y in range(8):
                #the logic works because it is a 8x8 board and the screen is 800x800
                pygame.draw.rect(screen, ("grey" if y % 2 - x % 2 == 0 else "teal"), (y*100 , x * 100,  100, 100))
                if board[x + y * 8] != 0:
                    pos_board[x + y * 8] = ((700-x * 100 ,700- y * 100))

    else:
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(screen, ("teal" if y % 2 - x % 2 == 0 else "grey"), (y*100 , x * 100,  100, 100))
                if board[x + y * 8] != 0:
                    pos_board[x + y * 8] = ((x * 100 , y * 100))


def render_pieces(board):        
    for piece in board:
        board[piece].render()
        
def get_random_key_value(dict):
    random_key = random.choice(list(dict.keys()))
    random_value = dict[random_key]
    return random_key, random_value
        
def play_moves():
    possible_moves_white = poss_moves(board, board_pieces, not color)
    # possible_moves_black = poss_moves(board, board_pieces, not color)
    # depth -= 1
    white_key, white_value = get_random_key_value(possible_moves_white)
    piece_white = board[white_key]
    board[white_key] = 0
    board[white_value] = piece_white
    draw_board()
    piece_board(board, board_pieces, pos_board, screen)
    render_pieces(board_pieces)
    pygame.display.flip
    
def check_check_white(board, move = None):
    black_moves = poss_moves(board, board_pieces, False)
    for x in black_moves:
        for y in x:
            if board[y] == 64:
                return True
    return False

def check_check_black(board, move = None):
    black_moves = poss_moves(board, board_pieces, False)
    for x in black_moves:
        for y in x:
            if board[y] == 65:
                return True
    return False
    
def calc_points():
    for x in board_pieces:
        if board % 2 == 0:
            points_white += board_pieces[x].value * 100
        else:
            points_black += board_pieces[x].value * 100
            
    return points_white, points_black


draw_board()
piece_board(board, board_pieces)
render_pieces(board_pieces)
clicked = False

possible_moves_white = poss_moves(board, board_pieces, color)
possible_moves_black = poss_moves(board, board_pieces, not color)
print(possible_moves_white)

print("------------------------------------")
first_poss_depth_first(board, board_pieces, pos_board, screen)
# play_2moves(10)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            break
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print(pygame.mouse.get_pos())
            posx, posy = pygame.mouse.get_pos()
            #r_pos stand for real pos
            #it is calculated by integer dividing by 100 so that the number will be rounded to 100
            if c:
                r_posx = 7 - posx//100
                r_posy = 7 - posy//100

            else:
                r_posx = posx//100
                r_posy = posy//100
            
            
            if clicked:
                print("clicked")
                pos_squares = possible_moves_white[n_posx + n_posx*8]
                if (r_posx + r_posy*8) in pos_squares: 
                    board[r_posx + r_posy * 8] = piecevalue
                    board[prev_x + prev_y * 8] = 0
                    draw_board()
                    board_pieces = piece_board(board, board_pieces, pos_board, screen)
                    board_pieces[r_posx + r_posy * 8].moved = True
                    render_pieces(board_pieces)
                    possible_moves_white = poss_moves(board, board_pieces, color)
                    white_check = check_check_black(board)
                    black_check = check_check_white(board)
                    print("white checked" if white_check else "")
                    print("black checked" if black_check else "")
                        # comment: )
                    play_moves()
                else:
                    board_pieces[prev_x + prev_y * 8].selected = False if board_pieces[prev_x + prev_y * 8].selected else True
                    draw_board()
                    render_pieces(board_pieces)
                    pass
                clicked = False
            else:
                if board[r_posx + r_posy * 8] != 0:
                    # print(r_posx, r_posy)
                    clicked = True
                    prev_x = r_posx
                    prev_y = r_posy
                    piecevalue = board[r_posx + r_posy * 8]
                    board_pieces[r_posx + r_posy * 8].selected = False if board_pieces[r_posx + r_posy * 8].selected else True
                    draw_board()
                    render_pieces(board_pieces)
                    n_posx =  prev_x
                    n_posy = 7 - prev_y
                    print(r_posx,)
    pygame.display.flip()


    # pygame.init()
 