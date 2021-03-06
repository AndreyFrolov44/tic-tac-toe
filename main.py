import pygame
from tic_tac_toe.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE
from tic_tac_toe.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
WIN.fill(WHITE)
pygame.display.update()


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
        clock.tick(FPS)

        if game.winner() is not None:
            print(f'Победил {game.winner()}')
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.restart()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
                elif not game.check_empty_el():
                    game.restart()
        game.update()
    pygame.quit()


main()

