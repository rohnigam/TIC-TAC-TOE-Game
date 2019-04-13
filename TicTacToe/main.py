import uuid
from TicTacToe.Game.game import Game
from TicTacToe.Game.gameStatus import GameStatus
from TicTacToe.Game.GameExceptions.invalidMove import InvalidMoveError


def main():
    user1 = uuid.uuid4()
    user2 = uuid.uuid4()

    new_game = Game(user1)

    player1 = new_game.set_game()

    player2 = new_game.join_game(user2)

    while new_game.check_game_status() == GameStatus.NotOver:
        choice = int(input('Enter 1 for player1 and 2 for player 2 to make a move  '))
        row, col = input('Enter move ').split()

        if choice == 1:
            current_player = player1
        elif choice == 2:
            current_player = player2
        else:
            print('Invalid player choice !')
            continue

        try:
            current_player.make_move(int(row), int(col))
        except InvalidMoveError as error:
            print(error)
            print('Try again\n\n')
        else:
            new_game.display_board()

    print('Game Over !')
    print(new_game.result())


if __name__ == '__main__':
    main()







