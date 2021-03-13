import pygame
import numpy as np
from .constants import COLS, ROWS, SQUARE_SIZE, BLACK, WIDTH, WHITE
from .piece import Piece


class Field:
    def __init__(self):
        self.field = []
        self.create_field()

    def draw_line(self, win):
        for i in range(ROWS):
            x = i * SQUARE_SIZE
            pygame.draw.line(win, BLACK, (x, 0), (x, WIDTH), 3)
            pygame.draw.line(win, BLACK, (0, x), (WIDTH, x), 3)
            pygame.display.update()

    def check_empty(self):
        field = np.array(self.field)
        return np.any(field == 0)

    def draw(self, win):
        self.draw_line(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.field[row][col]
                if piece != 0:
                    piece.draw(win)

    def draw_win_line(self, win, first, last):
        pygame.draw.line(win, BLACK, (first.x, first.y), (last.x, last.y), 4)

    def restart(self, win):
        self.field = []
        win.fill(WHITE)
        self.create_field()

    def create_field(self):
        for row in range(ROWS):
            self.field.append([])
            for col in range(COLS):
                self.field[row].append(0)

    def add_piece(self, row, col, type_piece):
        if self.field[row][col] == 0:
            self.field[row][col] = Piece(row, col, type_piece)
            return True
        else:
            return False

    def winner(self):
        field = np.array(self.field)
        win_arr = np.array([field.diagonal(), field[:, ::-1].diagonal()])
        for row_or_col in range(ROWS):
            win_arr = np.vstack([win_arr, self.field[row_or_col], field[:, row_or_col]])
        for win in win_arr:
            if 0 not in win:
                if np.all(np.unique([str(w) for w in win]).size == 1):
                    return win[0], win[-1]
        return None
