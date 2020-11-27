from app.Pos import Pos


class Block:

    def __init__(self, p1: Pos, p2: Pos):
        assert (p1.x <= p2.x and p1.y <= p2.y), "Invalid block position: p1=" + p1 + ", p2=" + p2
        self.p1 = p1
        self.p2 = p2

    def is_standing(self) -> bool:
        return self.p1.x == self.p2.x and self.p1.y == self.p2.y

    def left(self):
        if self.is_standing():
            self.dy(-2, -1)
        elif self.p1.x == self.p2.x:
            self.dy(-1, -2)
        else:
            self.dy(-1, -1)

    def right(self):
        if self.is_standing():
            self.dy(1, 2)
        elif self.p1.x == self.p2.x:
            self.dy(2, 1)
        else:
            self.dy(1, 1)

    def up(self):
        if self.is_standing():
            self.dx(-2, -1)
        elif self.p1.x == self.p2.x:
            self.dx(-1, -1)
        else:
            self.dx(-1, -2)

    def down(self):
        if self.is_standing():
            self.dx(1, 2)
        elif self.p1.x == self.p2.x:
            self.dx(1, 1)
        else:
            self.dx(2, 1)

    # Returns a block where the X coordinates of p1 and p2 are changed by d1 and d2, respectively.
    def dx(self, d1, d2):
        return Block(self.p1.dx(d1), self.p2.dx(d2))

    # Returns a block where the Y coordinates of p1 and p2 are changed by d1 and d2, respectively.
    def dy(self, d1, d2):
        return Block(self.p1.dy(d1), self.p2.dy(d2))
