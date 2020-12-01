#  Copyright (c) 2020. Abhilshit Soni

from app.position import Position
import json


class Block:
    """
    A Block object representing a Bloxorz block containing 2 bricks. In a standing position this block will occupy
    one position. In laying position this block will occupy 2 positions one for each brick.
    """

    def __init__(self, p1: Position, p2: Position):
        # Assert that p1 is lexicographically smaller than or equal to p2. P<p2 in laying condition. P1 == p2 in standing condition.
        assert (p1.x <= p2.x and p1.y <= p2.y), "Position of blok is not valid: p1=" + p1 + ", p2=" + p2
        self.p1 = p1
        self.p2 = p2

    def is_standing(self) -> bool:
        """
        Returns a boolean value is the block is standing or not
        :return: True if standing else flase
        """
        return self.p1.x == self.p2.x and self.p1.y == self.p2.y

    def left(self):
        """
        Move Left operation
        :return: Block after left move
        """
        if self.is_standing():
            return self.dy(-2, -1)
        elif self.p1.x == self.p2.x:
            return self.dy(-1, -2)
        else:
            return self.dy(-1, -1)

    def right(self):
        """
        Move Right operation
        :return: Block after right move
        """
        if self.is_standing():
            return self.dy(1, 2)
        elif self.p1.x == self.p2.x:
            return self.dy(2, 1)
        else:
            return self.dy(1, 1)

    def up(self):
        """
        Move up operation
        :return: Block after up move
        """
        if self.is_standing():
            return self.dx(-2, -1)
        elif self.p1.x == self.p2.x:
            return self.dx(-1, -1)
        else:
            return self.dx(-1, -2)

    def down(self):
        """
        Move down operation
        :return: Block after down move
        """
        if self.is_standing():
            return self.dx(1, 2)
        elif self.p1.x == self.p2.x:
            return self.dx(1, 1)
        else:
            return self.dx(2, 1)

    # Returns a block where the X coordinates of p1 and p2 are changed by d1 and d2, respectively.
    def dx(self, d1, d2):
        return Block(self.p1.dx(d1), self.p2.dx(d2))

    # Returns a block where the Y coordinates of p1 and p2 are changed by d1 and d2, respectively.
    def dy(self, d1, d2):
        return Block(self.p1.dy(d1), self.p2.dy(d2))

    def __str__(self):
        return json.dumps([str(self.p1), str(self.p2)])
