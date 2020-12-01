#  Copyright (c) 2020. Abhilshit Soni

from app.block import Block
from app.move import Move
from app.terrain import Terrain
from app.a_star_solver import A_Star_Solver
import time
import json


class Game:
    """
       A Game class that is responsible for building a game from the terrain information obtained from a level file.
        It also has a reference to A* Solver Agent  which can search the path to obtain a solution
    """
    def __init__(self, terrain):
        """
        Initializes a Game Object with a terrain that is constructed based on a level file
        :param terrain:
        """
        self.terrain = terrain
        self.a_star_solver_agent = A_Star_Solver(h_func="Eucledian")
        #self.a_star_solver_agent =  A_Star_Solver(h_func="Chebyshev")

    def solve_game(self):
        """
            Solves the game using A* Solver Agent
        """
        print("############### Solving Game with A*  Algorithm ############")
        start_time = time.time()
        paths = self.a_star_solver_agent.solve(self.terrain)
        print("--- Solved using A* in %s seconds ---" % (time.time() - start_time))
        print("Solution: ", self.pretty_print_paths(paths))

    def test_game(self):
        """
        Utility Functions to test the game states
        """
        print(json.dumps(self.terrain.map))
        print("Putting Block at Start in standing position")
        b = Block(self.terrain.start, self.terrain.start)
        b1 = b.down()
        print("done? ", self.terrain.done(b1))
        b2 = b1.down()
        print(b2)
        print(b2.is_standing())
        print(b.left())
        print(b.right())
        print(b.up())
        print(b.down())
        print(self.terrain.can_hold(b.left()))
        print(self.terrain.can_hold(b.right()))
        print(self.terrain.can_hold(b.up()))
        print(self.terrain.can_hold(b.down()))

    def pretty_print_paths(self, paths):
        """
        Accepts a list of @Move object representing moves taken to reach to the goal from start and
        returns a pretty printed string represnting the sequence of moves required to reach the goal from start state
        :param paths:
        :return: String of pretty printed path
        """
        path_str = ""
        for i, path in enumerate(paths):
            if path is None:
                continue
            elif path == Move.Right:
                path_str = path_str + " Right "
            elif path == Move.Left:
                path_str = path_str + " Left "
            elif path == Move.Down:
                path_str = path_str + " Down "
            elif path == Move.Up:
                path_str = path_str + " Up "
            if i < len(paths) - 1:
                path_str = path_str + "->"

        return path_str

if __name__ == '__main__':
    # Initialize terrain
    terrain = Terrain(level_file="../resources/level01.txt")
    print("Start at:" + str(terrain.start))
    print("Goal at:" + str(terrain.goal))
    # Create Game
    game = Game(terrain)
    #Solve Game by finding sequence path of moves required to reach to goal from start
    game.solve_game()
