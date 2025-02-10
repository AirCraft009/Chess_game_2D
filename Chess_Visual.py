from Chess_back_handling import *
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

def draw_board():
    for y in range(8):
        for x in range(8):
            pygame.draw.rect(screen, ("grey" if y % 2 - x % 2 == 0 else "teal"), (y*100 , x * 100,  100, 100))
            poss_board[x + y * 8] = ((x*100 ,700-y * 100))
    
draw_board()
pieces = get_pieces(poss_board, screen, images)
render_pieces(pieces)
print(poss_moves(board, pieces, True))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            play_random(screen, poss_board, images)
    pygame.display.flip()