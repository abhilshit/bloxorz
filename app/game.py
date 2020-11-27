from app.Block import Block
from app.Terrain import Terrain


class Game:
    if __name__ == '__main__':
        terrain = Terrain()
        print("Start at:" + str(terrain.start))
        print("Goal at:" + str(terrain.goal))
        print("Putting Block at Start in standing position")
        b = Block(terrain.start, terrain.start)
        b1 = b.down()
        b2 = b1.down()
        print(b2)
        print(b2.is_standing())
        print(b.left())
        print(b.right())
        print(b.up())
        print(b.down())
        print(terrain.can_hold(b.left()))
        print(terrain.can_hold(b.right()))
        print(terrain.can_hold(b.up()))
        print(terrain.can_hold(b.down()))