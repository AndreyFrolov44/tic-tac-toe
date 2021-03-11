from .field import Field


class Game:
    def __init__(self, win):
        self.win = win
        self.field = Field()
        self.turn = "x"

    def update(self):
        self.field.draw(self.win)

    def winner(self):
        return self.field.winner()

    def select(self, row, col):
        piece = self.field.add_piece(row, col, self.turn)
        if piece:
            self.change_turn()

    def change_turn(self):
        if self.turn == "x":
            self.turn = "o"
        else:
            self.turn = "x"

