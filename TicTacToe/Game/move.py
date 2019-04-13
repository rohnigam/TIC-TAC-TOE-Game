from . import player


class Move:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.move_player: player.Player = None

    @property
    def move_player(self):
        return self._move_player

    @move_player.setter
    def move_player(self, move_player):
        self._move_player = move_player

