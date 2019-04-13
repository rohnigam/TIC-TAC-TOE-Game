import enum


class GameStatus(enum.Enum):
    NotOver = 1
    PlayerOneWon = 2
    PlayerTwoWon = 3
    Draw = 4
    