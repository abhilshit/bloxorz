#  Copyright (c) 2020. Abhilshit Soni

from app.position import Position
from app.block import Block
from app.move import Move
import json


class Terrain:
    """
    Class Terrain represents the terrain of the game. Terrain contains a
        1. map of traversable and non-traversable areas, represented by True and False boolean values
        2. A start location representing initial location of the bloxorz block (in standing position at start)
        3. A goal location representing the target/ goal to be reached inorder to solve the game
        4. width representing the total columns of the terrain of level-1 bloxorz
        5. height representing the total rows of the terrain of level-1 bloxorz

    """
    map = None  # boolean map of traversable and non-traversable areas
    start = None # start location of the bloxorz block
    goal = None # goal location of the bloxorz block to be reached in order to solve the game level-1
    width = 10  # width for level 1 (no of columns)
    height = 6  # height for level 1 (no of rows)

    def __init__(self, level_file="resources/level01.txt"):
        """
        initializes Terrain object by parsing the level file provided as an input.
        :param level_file: level file representing the bloxorz level 1 positions
        """
        self.parse_terrain(level_file)

    def can_hold(self, b: Block) -> bool:
        """
        Returns true if Terrain can hold the block completely. As in, both the cubes of bloxorz block should be at the
        legal locations on the terrain map represented by boolean True values in the map.
        :param b: Block object to be verified if it is occupying legal/allowed positions.
        :return: True if Terrain can hold the block completely, else return False
        """
        try:
            can_hold = self.map[b.p1.x][b.p1.y] and self.map[b.p2.x][b.p2.y]
        except IndexError:
            can_hold = False  # print("Warning: "+ str(b.p1) + " or " + str(b.p2) + " is out of range !!")

        return can_hold

    def neighbours(self, b: Block) -> list:
        """
        Gets the neighbours (potential block positions) based on the allowed moves (up,down,left,right)
         from the current position of the block
        :param b: Block object whose neighbours are to be returned
        :return: list of (Block, Move) Tuple representing neighbouring blocks and move required to reach their
        respective block positions
        """
        return [(b.up(), Move.Up), (b.down(), Move.Down), (b.left(), Move.Left), (b.right(), Move.Right)]

    def legal_neighbors(self, b: Block) -> list:
        """
        Filters the list of neighbours by checking if the neighbours are on legally allowed postions on the terrain map
        :param b: Block object whose legal neighbours are to be returned
        :return: list of (Block, Move) Tuple representing legally allowed neighbouring blocks and move required to reach
         their respective block positions
        """
        return [(n, move) for (n, move) in self.neighbours(b) if self.can_hold(n)]

    def done(self, b: Block) -> bool:
        """
        Returns true if the current block is at the goal position. The goal is reached only if the Block is in standing
        position and if the position of the block is equal to position of the goal.
        :param b: Block object to be verified whether it has reached the goal
        :return: True if block has reached the goal and is in a standing postion,  else return False
        """
        return b.is_standing() and b.p1.x == self.goal.x and b.p1.y == self.goal.y

    def parse_terrain(self, level_file):
        """
        Parses the level file, initializes the boolean map of the Terrain object representing allowed traversable
        positions, sets up the start and goal postions based on location of S and T un the level file.
        :param level_file:
        """
        file = open(level_file, "r")
        self.map = []
        for x, line in enumerate(file):
            row = []
            for y, char in enumerate(line):
                if char == 'S':
                    self.start = Position(x, y)
                    row.append(True)
                elif char == 'T':
                    self.goal = Position(x, y)
                    row.append(True)
                elif char == '0':
                    row.append(True)
                elif char == '-':
                    row.append(False)
            self.map.append(row)
        file.close()
        # print("Terrain map created")
        # print(json.dumps(self.map))
