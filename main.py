import pygame
from surakarta.constants import WIDTH,HEIGHT,SQUARE_SIZE,RED, WHITE, W_BCKGRND, H_BCKGRND, BOARD_POS
from surakarta.game import Game
from minimax.minimax_algorithm import minimax


FPS = 60

WIN = pygame.display.set_mode((W_BCKGRND,H_BCKGRND))
pygame.display.set_caption('Surakarta Board Game')
# background_image = pygame.image.load("image/surakarta_board.jpg").convert()

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        # WIN.blit(background_image, [0, 0])

        # pygame.display.flip()
        clock.tick(FPS)

        # if game.turn == WHITE:
        #     value, new_board = minimax(game.get_board(), 2, WHITE, game)
        #     game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()