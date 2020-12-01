#  Copyright (c) 2020. Abhilshit Soni
from math import sqrt

from app.block import Block
from app.node import Node
from app.terrain import Terrain


class A_Star_Solver:
    """
    A_Star_Solver represents a solver agent that is capable to find sequence of moves (or path) required to reach from
    Start to Goal using an A* algorithm. It uses Chebyshev distance  (aka. Chessboard distance) by default as a Heuristic
    Function
    """

    # Heuristic Function to be used can be either of either 'Eucledian' or 'Chebyshev' distance.
    heuristic_functions = ["Eucledian", "Chebyshev"]

    def __init__(self, h_func="Chebyshev"):
        """
        Initialize the solver agent with default Chebyshev distance as Heuristic function
        :param h_func: The Heuristic function to be used
        """
        self.h_func = h_func
        assert self.h_func in self.heuristic_functions, "Heuristic Function can be either 'Eucledian' or 'Chebyshev' "

    def solve(self, terrain: Terrain) -> list:
        """
        Solver that solves the bloxorz using A*
        :param terrain:
        :return:
        """
        open_list = []  # Initialize open list
        closed_list = []  # Initialize closed list

        start_pos = terrain.start
        start_block = Block(start_pos, start_pos)
        start_node = Node(start_block, move=None, parent=None, f=0, g=0, h=0) #Initialize a start Node object

        goal_pos = terrain.goal
        goal_block = Block(goal_pos, goal_pos)

        open_list.append(start_node) #add start Node to the open list

        while len(open_list) > 0:
            # Get the current node
            current_node = open_list[0]
            current_index = 0

            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            open_list.pop(current_index)
            closed_list.append(current_node)

            if terrain.done(current_node.block):
                path = []
                current = current_node
                # BackTrack Moves
                while current is not None:
                    path.append(current.move)
                    current = current.parent
                return path[::-1]  # Return reversed order of Moves
            children = self.get_children(current_node, terrain)

            for child in children:

                # continue if child is on the closed list
                if child in closed_list:
                    continue

                # Create the f, g, and h values
                child.g = current_node.g + 1

                # Using Eucledian distance as heuristic function
                if self.h_func == "Eucledian":
                    child.h = sqrt(((child.block.p2.x - goal_block.p2.x) ** 2) + ((child.block.p2.y - goal_block.p2.y) ** 2))

                # Using Chebyshev distance as heuristic function
                if self.h_func == "Chebyshev":
                    hn1 = max(abs(child.block.p1.x - goal_block.p1.x), abs(child.block.p1.y - goal_block.p1.y))
                    hn2 = max(abs(child.block.p2.x - goal_block.p2.x), abs(child.block.p2.y - goal_block.p2.y))
                    child.h = max(hn1, hn2)

                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)

    def get_children(self, current_node: Node, terrain: Terrain):
        """
        Gets Children of current Node by querying legal neighbours of a node block.
        :param current_node:
        :param terrain:
        :return:
        """
        legal_neighbours = terrain.legal_neighbors(current_node.block)
        children = []
        for (legal_neighbour, legal_move) in legal_neighbours:
            child = Node(block=legal_neighbour, move=legal_move, parent=current_node)
            children.append(child)
        return children
