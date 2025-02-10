from fen_read import read_Fen
from piece_board import piece_board, Piece
from evalution import *
from possible_moves import poss_moves
import random

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
    
def get_board():
    return board

def render_pieces(board_pieces):
    for piece in board_pieces:
        board_pieces[piece].render()

def update_board(screen, move: tuple[int, int], pos_board: dict, images: list):
    play_move(move)    
    board_pieces = piece_board(board, pos_board, screen, images)
    render_pieces(board_pieces)
    
    
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

def play_random(screen, pos_board, images):
    rand_square, poss_square = get_rand_dict_item(get_moves(pos_board, screen, images))
    update_board(screen, (rand_square, poss_square), pos_board, images)
    

    

    
    
    
    
