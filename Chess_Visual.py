from Chess_back_handling import *
from possible_moves import first_poss_depth_first
import pygame
import random

image_path = "images/"
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess")
pygame.init()
board = get_board()
poss_board = {}

images = [
    pygame.image.load(image_path + "white_pawn.png").convert_alpha(),
    pygame.image.load(image_path + "black_pawn.png").convert_alpha(),
    pygame.image.load(image_path + "white_knight.png").convert_alpha(),
    pygame.image.load(image_path + "black_knight.png").convert_alpha(),
    pygame.image.load(image_path + "white_bishop.png").convert_alpha(),
    pygame.image.load(image_path + "black_bishop.png").convert_alpha(),
    pygame.image.load(image_path + "white_rook.png").convert_alpha(),
    pygame.image.load(image_path + "black_rook.png").convert_alpha(),
    pygame.image.load(image_path + "white_queen.png").convert_alpha(),
    pygame.image.load(image_path + "black_queen.png").convert_alpha(),
    pygame.image.load(image_path + "white_king.png").convert_alpha(),
    pygame.image.load(image_path + "black_king.png").convert_alpha()
]

    
poss_board = draw_board(screen)
pieces = get_pieces(poss_board, screen, images)
render_pieces(pieces)
# print(poss_moves(board, pieces, False))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board = first_poss_depth_first(board, pieces, poss_board, screen, images)
            set_board(board)
            update_board(screen, (0, 0), poss_board, images)
            # print(is_checked(board, get_pieces(poss_board, screen, images)))
    pygame.display.flip()