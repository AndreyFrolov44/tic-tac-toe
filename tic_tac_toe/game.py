from .field import Field
import pygame


class Game:
    def __init__(self, win):
        self.win = win
        self.field = Field()
        self.turn = "x"

    def update(self):
        self.field.draw(self.win)

    def winner(self):
        winner = self.field.winner()
        if winner is not None:
            self.field.draw_win_line(self.win, winner[0], winner[-1])
            return winner[0]
        return None

    def check_empty_el(self):
        return self.field.check_empty()

    def restart(self):
        self.field.restart(self.win)

    def select(self, row, col):
        piece = self.field.add_piece(row, col, self.turn)
        if piece:
            self.change_turn()

    def change_turn(self):
        if self.turn == "x":
            self.turn = "o"
        else:
            self.turn = "x"

