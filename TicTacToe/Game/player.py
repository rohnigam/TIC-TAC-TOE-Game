from . import game
from . import move


class Player:
    """
    This class defines a player in a game of tic-tac-toe.
    """
    def __init__(self, my_num: int, player_name: str):
        self.my_num = my_num
        self.player_name = player_name

        self.my_game: game.Game = None

    def make_move(self, row: int, col: int) -> None:
        """

        :param row: integer signifying row on board
        :param col: integer signifying col on board
        :return: None
        """

        new_move = move.Move(row, col)
        new_move.move_player = self
        self.my_game.game_board.make_move(new_move)

    def __str__(self):
        return self.player_name


