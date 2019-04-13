from typing import List, Tuple
from termcolor import colored
from .player import Player
from .gameStatus import GameStatus
from .move import Move
from TicTacToe.Game.GameExceptions.invalidMove import InvalidMoveError


class Board:
    """
    This is the implementation for a game board in a
    game of tic-tac-toe
    """

    def __init__(self, player1: Player, player2: Player, board_size: int):
        self.player1 = player1
        self.player2 = player2
        self.board_size = board_size

        self.matrix: List[List[int]] = [[0]*self.board_size for _ in range(self.board_size)]
        self.player_turn = self.player1
        self.moves_list: List[Move] = []

        self.empty_boxes: int = self.board_size * self.board_size
        self.game_status: GameStatus = GameStatus.NotOver

        self.row_sums = [0]*self.board_size
        self.col_sums = [0]*self.board_size
        self.primary_diagonal_sum = 0
        self.secondary_diagonal_sum = 0

    def make_move(self, new_move: Move) -> None:
        """
        This method validates a move initiated by a player,
        if valid makes the move on the board. Also, updates
        the state of game, if it is over or not.

        :param new_move: Move initiated
        :return: None
        :throws: InvalidMoveError exception if the move made is invalid
        """

        valid_move, invalid_reason = self.is_move_valid(new_move)

        if valid_move:
            self.matrix[new_move.row][new_move.col] = new_move.move_player.my_num

            self.update_sums(new_move)

            self.moves_list.append(new_move)
            self.toggle_turn()
            self.empty_boxes -= 1

            self.game_status = self.check_game_status()

        else:
            raise InvalidMoveError(invalid_reason)

    def toggle_turn(self) -> None:
        """
        Toggle's the player turn from one player to another

        :return: None
        """

        if self.player_turn == self.player1:
            self.player_turn = self.player2
        else:
            self.player_turn = self.player1

    def is_move_valid(self, new_move: Move) -> Tuple[bool, str]:
        """
        This api checks if a move initiated is valid or not and returns
        a boolean result along with an error string, describing the reason
        why the move is invalid.

        :param new_move: Move initiated
        :return: Tuple of bool and string
        """

        if self.player_turn != new_move.move_player:
            return False, 'Move out of turn'

        if not self.is_move_within_bounds(new_move):
            return False, 'Move out of the bounds of board'

        if self.matrix[new_move.row][new_move.col]:
            return False, 'Block already filled'

        return True, 'Success'

    def is_move_within_bounds(self, new_move: Move) -> bool:
        """
        This api validates whether a move is
        within the bounds of the board or not.

        :return: bool, True if within bounds
        """

        if 0 <= new_move.row < self.board_size and 0 <= new_move.col < self.board_size:
            return True

        return False

    def check_game_status(self) -> GameStatus:
        """
        This api checks the game status based on the
        current state of the board.

        :return: GameStatus
        """

        if not self.moves_list:
            return GameStatus.NotOver

        latest_move = self.moves_list[-1]

        '''
        if at all there is a winner, it has to be the guy
        who just made the move
        '''
        if self.has_player_won(latest_move):
            return GameStatus.PlayerOneWon if latest_move. move_player == self.player1 else GameStatus.PlayerTwoWon
        elif not self.empty_boxes:
            # no boxes left in the game, match draw
            return GameStatus.Draw
        else:
            return GameStatus.NotOver

    def update_sums(self, new_move: Move) -> None:
        """
        This api updates the row_sums, col_sums and primary and
        secondary diagonal sums also if applicable.

        :param new_move: Move made
        :return: None
        """

        self.row_sums[new_move.row] += new_move.move_player.my_num
        self.col_sums[new_move.col] += new_move.move_player.my_num

        # check if the new move lies on the primary diagonal
        if new_move.row == new_move.col:
            self.primary_diagonal_sum += new_move.move_player.my_num

        # check if the new move lies on the secondary diagonal
        if new_move.row + new_move.col == self.board_size -1:
            self.secondary_diagonal_sum += new_move.move_player.my_num

    def has_player_won(self, latest_move: Move) -> bool:
        """
        This api checks if the move made has won the player the match.
        A player wins if he has all his entries in a row, col, or
        one of the two diagonals.

        :param latest_move: Move played
        :return: bool, True if player has won
        """

        if abs(self.row_sums[latest_move.row]) == self.board_size or \
            abs(self.col_sums[latest_move.col]) == self.board_size or \
            abs(self.primary_diagonal_sum) == self.board_size or \
            abs(self.secondary_diagonal_sum) == self.board_size:
            return True

        return False

    def __str__(self):
        board_str = ''
        for row in self.matrix:
            for entry in row:
                if entry == 1:
                    board_str += colored('%5s'%'X', 'red')
                elif entry == -1:
                    board_str += colored('%5s'%'O', 'blue')
                else:
                    board_str += colored('%5s'%'E', 'green')

            board_str += '\n'

        return board_str


