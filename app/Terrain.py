from app.Pos import Pos
from app.Block import Block
from app.Moves import Moves
import json


class Terrain:
    map = None
    start = None
    goal = None
    width = 10  # width for level 1
    height = 6  # height for level 1
    at = None

    def __init__(self, level_file="../resources/level01.txt"):
        self.parse_terrain(level_file)

    def can_hold(self, b: Block) -> bool:
        return self.map[b.p1.x][b.p1.y] and self.map[b.p2.x][b.p2.y]

    def neighbors(self, b: Block) -> list:
        [(b.up(), Moves.Up), (b.down(), Moves.Down), (b.left(), Moves.Left), (b.right(), Moves.Right)]

    def legal_neighbors(self, b: Block) -> list:
        return [(n,move) for (n,move) in self.neighbours(b) if self.can_hold(n)]

    def parse_terrain(self, level_file):
        file = open(level_file, "r")
        self.map = []
        for x, line in enumerate(file):
            row = []
            for y, char in enumerate(line):
                if char == 'S':
                    self.start = Pos(x, y)
                    self.at = Pos(x, y)
                    row.append(True)
                elif char == 'T':
                    self.goal = Pos(x, y)
                    row.append(True)
                elif char == '0':
                    row.append(True)
                else:
                    row.append(False)
            self.map.append(row)
        file.close()
        print("Terrain map created")
        print(json.dumps(self.map))



