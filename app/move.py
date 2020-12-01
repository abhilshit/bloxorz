#  Copyright (c) 2020. Abhilshit Soni

import enum


class Move(enum.Enum):
    """
    Enumerations of Moves allowed for the Bloxorz Block in the game
    Allowed moves are Left, Right, Up, Down
    """
    Left = 1
    Right = 2
    Up = 3
    Down = 4
