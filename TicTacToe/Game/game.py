import uuid
from .player import Player
from .board import Board
from .gameStatus import GameStatus


class Game:
    """
    This is the implementation for a game of tic-tac-toe
    between two players.
    """

    def __init__(self, user_id1):
        self.player1 = Player(1, 'Player1')
        self.player2 = Player(-1, 'Player2')
        self.player1.my_game = self
        self.player2.my_game = self

        self.game_board: Board = Board(self.player1, self.player2, 3)
        self.user_id1: uuid.UUID = user_id1
        self.user_id2: uuid.UUID = None

    def set_game(self) -> Player:
        """
        Sets a game up with one player

        :return: Player for user1
        """
        return self.player1

    def join_game(self, user_id2) -> Player:
        """
        This api can be used by a user to join an already setup game.

        :param user_id2: uuid.UUID
        :return: Player for user2
        """
        self.user_id2 = user_id2
        return self.player2

    def check_game_status(self) -> GameStatus:
        """
        This api checks the status of the game.

        :return: GameStatus
        """

        return self.game_board.check_game_status()

    def display_board(self) -> None:
        """
        Displays the board on the terminal.

        :return: None
        """

        print(self.game_board)

    def result(self) -> str:
        """
        This api returns the result of the game.

        :return: result string
        """

        current_game_status = self.check_game_status()
        if current_game_status == GameStatus.PlayerOneWon:
            return '%s WON'%self.player1
        elif current_game_status == GameStatus.PlayerTwoWon:
            return '%s WON'%self.player2
        elif current_game_status == GameStatus.Draw:
            return 'Khhichdi'
        else:
            return 'Game ON'
