import pygame
from .constants import SQUARE_SIZE, WHITE, BLACK


class Piece:
    PADDING = 30
    OUTLINE = 2

    def __init__(self, row, col, type_piece):
        self.row = row
        self.col = col
        self.type = type_piece
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        if self.type == "o":
            radius = SQUARE_SIZE // 2 - self.PADDING
            pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.OUTLINE)
            pygame.draw.circle(win, WHITE, (self.x, self.y), radius)
        if self.type == "x":
            pygame.draw.line(win, BLACK, (SQUARE_SIZE * self.col + self.PADDING, SQUARE_SIZE * self.row + self.PADDING), (SQUARE_SIZE * self.col + SQUARE_SIZE - self.PADDING, SQUARE_SIZE * self.row + SQUARE_SIZE - self.PADDING), 3)
            pygame.draw.line(win, BLACK, (SQUARE_SIZE * self.col + self.PADDING, SQUARE_SIZE * self.row + SQUARE_SIZE - self.PADDING), (SQUARE_SIZE * self.col + SQUARE_SIZE - self.PADDING, SQUARE_SIZE * self.row + self.PADDING), 3)

    def __repr__(self):
        return self.type
