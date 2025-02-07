import random
import time
import pygame
from fen_read import read_Fen
from possible_moves import poss_moves




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


     
# load images
white_Pawn = pygame.image.load('white_pawn.png').convert_alpha()
black_Pawn = pygame.image.load('black_pawn.png').convert_alpha()
white_Knight = pygame.image.load('white_knight.png').convert_alpha()
black_Knight = pygame.image.load('black_knight.png').convert_alpha()
white_Bishop = pygame.image.load('white_bishop.png').convert_alpha()
black_Bishop = pygame.image.load('black_bishop.png').convert_alpha()
white_Rook = pygame.image.load('white_rook.png').convert_alpha()
black_Rook = pygame.image.load('black_rook.png').convert_alpha()
white_Queen = pygame.image.load('white_queen.png').convert_alpha()
black_Queen = pygame.image.load('black_queen.png').convert_alpha()
white_King = pygame.image.load('white_king.png').convert_alpha()
black_King = pygame.image.load('black_king.png').convert_alpha()

    
def piece_board(board, allocated_board):
    """
    Populates the allocated_board dictionary with Piece objects, given a board and piece images.
    using th piece_map dictionary and because it is a O(1) operation to look up a value 
    it is very efficient

    Parameters:
        board (dict): A dictionary representing the chess board, with keys as the space number and values as the piece that is on that space.
        allocated_board (dict): An empty dictionary to store the created Piece objects.

    Returns:
        allocated_board (dict): The populated allocated_board dictionary.
    """
    allocated_board.clear()

    piece_map = {
        2:  ("white", 1, 1, white_Pawn),
        3:  ("black", 1, 1, black_Pawn),
        4:  ("white", 2, 2, white_Knight),
        5:  ("black", 2, 2, black_Knight),
        8:  ("white", 3, 3, white_Bishop),
        9:  ("black", 3, 3, black_Bishop),
        16: ("white", 4, 4, white_Rook),
        17: ("black", 4, 4, black_Rook),
        32: ("white", 5, 5, white_Queen),
        33: ("black", 5, 5, black_Queen),
        64: ("white", 6, 6, white_King),
        65: ("black", 6, 6, black_King),
    }
    
    for x, piece in board.items():
        if piece in piece_map:
            color, value1, value2, image = piece_map[piece]
            allocated_board[x] = Piece(pos_board[x][0], pos_board[x][1], color, piece, value1, value2, image, x)
    return allocated_board
    
    

    



    
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
            
           
class Piece(object):
    def __init__(self, x, y, color, type, step, value, image, space):
        self.x = x
        self.y = y
        self.color = color
        self.type = type
        self.step = step
        self.value = value
        self.image = image
        self.space = space
        self.selected = False
        self.moved = False
    
    def render(self, depth = 1):
        	
        screen.blit(self.image, (self.x, self.y))
        if self.selected:
            pygame.draw.rect(screen, ("red"), (self.x, self.y, 100, 100), 5)
            pygame.display.update()


def render_pieces(board):        
    for piece in board:
        board[piece].render()
        
def play_2moves(depth):
    if depth == 0:
        return 0
    
    possible_moves_white = poss_moves(board, board_pieces, color)
    possible_moves_black = poss_moves(board, board_pieces, not color)
    
    depth -= 1
    b = False
    w = False
    while True:

        black = random.randint(0, 63)
        white = random.randint(0, 63)
        if board[black]%2 == 1:
            b = True
        if board[white]%2 == 0:
            w = True
        if b and w:
            break
    rand_square_white = random.choice(possible_moves_white[white])
    rand_square_black = random.choice(possible_moves_black[black])
    piece_black = board[black]
    piece_white = board[white]
    board[white] = 0
    board[rand_square_white] = piece_white
    board[black] = 0
    board[rand_square_black] = piece_black
    time.sleep(1)
    play_2moves(depth)
    draw_board()
    piece_board(board, board_pieces)
    render_pieces(board_pieces)
    pygame.display.flip
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    


draw_board()
piece_board(board, board_pieces)
render_pieces(board_pieces)
clicked = False

possible_moves_white = poss_moves(board, board_pieces, color)
possible_moves_black = poss_moves(board, board_pieces, not color)
print(possible_moves_white)
play_2moves(10)
"""
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
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
                rand_square = possible_moves_white[n_posx + n_posx*8]
                print(n_posx + n_posy*8)
                if (n_posx + n_posx*8) in rand_square: 
                    board[r_posx + r_posy * 8] = piecevalue
                    board[prev_x + prev_y * 8] = 0
                    draw_board()
                    board_pieces = piece_board(board, board_pieces)
                    board_pieces[r_posx + r_posy * 8].moved = True
                    render_pieces(board_pieces)
                    possible_moves_white = poss_moves(board, board_pieces, color)
                    possible_moves_black = poss_moves(board, board_pieces, not color)
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
"""


    # pygame.init()
 