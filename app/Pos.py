import json


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dx(self, d):
        return Pos(self.x + d, self.y)

    def dy(self, d):
        return Pos(self.x, self.y + d)

    def __str__(self):
        return json.dumps([self.x, self.y])
