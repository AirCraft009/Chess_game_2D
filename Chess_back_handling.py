from fen_read import read_Fen
from piece_board import piece_board, Piece
from evalution import *
from possible_moves import poss_moves
import random
import pygame
poss_board = {}

turn = 0
global board_pieces, white_moves, black_moves

fen = "rnbqkbnr/pppppppp/8/8/8/8/8/RNBQKBNR"
board = read_Fen(fen, {})

def get_pieces(pos_board, screen, images):
    return piece_board(board, pos_board, screen, images)

def play_move(move: tuple[int, int]):
    piece_val = board[move[0]]
    board[move[0]] = 0
    board[move[1]] = piece_val
    turn == 0 if turn == 1 else 1
    
    
def set_board(board1):
    board = board1
    
def draw_board(screen):
    for y in range(8):
        for x in range(8):
            pygame.draw.rect(screen, ("grey" if y % 2 - x % 2 == 0 else "teal"), (y*100 , x * 100,  100, 100))
            poss_board[x + y * 8] = ((x*100 ,700-y * 100))
    return poss_board
    
def get_board():
    return board

def render_pieces(board_pieces):
    for piece in board_pieces:
        board_pieces[piece].render()

def update_board(screen, move: tuple[int, int], pos_board: dict, images: list):
    play_move(move)    
    board_pieces = piece_board(board, pos_board, screen, images)
    render_pieces(board_pieces)
    return
    
    
def get_rand_dict_item(dic: dict):
    rand_item = random.choice(list(dic.items()))
    return rand_item
        
def get_moves(pos_board, screen, images):
    board_pieces = piece_board(board, pos_board, screen, images)
    if turn == 0:
        white_moves = poss_moves(board, board_pieces, True)
        print(white_moves)
        return white_moves
    else:
        black_moves = poss_moves(board, board_pieces, False)
        return black_moves

def play_random(screen, images):
    pos_board = draw_board(screen)
    rand_square, poss_squares = get_rand_dict_item(get_moves(pos_board, screen, images))
    try:
        poss_square = random.choice(poss_squares)
        pos_board = draw_board(screen)
        update_board(screen, (rand_square, poss_square), pos_board, images)
        # turn == 0 if turn == 1 else 1
        return pos_board
    except Exception as e:
        play_random(screen, images)

    

    

    
    
    
    
