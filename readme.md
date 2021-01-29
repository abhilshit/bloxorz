## Solving Bloxorz using A* (A-star) Algorithm

Bloxorz is a 3-D block sliding puzzle game that consists of a terrain that is built
by 1×1 tile with a special shape and size, and a 1×1×2 size block. This game is a
single agent path-finding problem that involves moving the block from its initial
position using four directions **_(right, left, up, and down)_** and ensuring that its ends
are always within the terrain boundary, until it falls into a 1×1 square hole in the
terrain that represents our goal state.

The block can be in three states, standing, lying horizontally, and lying
vertically. When the block reaches the hole, it must be in standing state to fall in it.
The level-1 of the game begins with the size of the terrain as 6×10 rows and
columns, starting position is at row 2 and column 2 or as user determines it, and
goal position is at row 5 and column 8. The shape of the terrain in the first level is
shown.

This is an implemntation of the A* Algorithm using Chebeshev distance as a heuristic to solve the game of Bloxorz as mentioned in the paper **Game of Bloxorz Solving Agent Using Informed and Uninformed Search Strategies** https://www.sciencedirect.com/science/article/pii/S187705091932160X authored by Tahani Q. Alhassan , Shefaa S. Omar , Lamiaa A. Elrefaei. Refer the References section below for more details. 

## Pre requisites

- Python 3.7
```bash
$ python --version or python -V
```

> **Note**: This game is build & taken reference from playing lvl1 stage on miniclip 
>game at
https://www.miniclip.com/games/bloxorz/en/#
>
## How to Run
Clone the repo and execute the following steps to runn
Steps to run
1. Navigate to <bloxorz_project_dir>/app   - >    
2. run the command   - >    PYTHONPATH=../ python game.py

  E.g.
```bash
>> cd <bloxorz_project_dir>/app
>> PYTHONPATH=../ python game.py
```
Alternatively, you can checkout and import the project in pycharm and run game.py

> **Note**: level-1 of Bloxorz game is implemented using A* algorithm to find fast and Optimal solution.

## OutPut
It will output the moves required to solve Bloxorz - Level-1

```bash
>>PYTHONPATH=../ python game.py
Start at:[1, 1]

Goal at:[4, 7]

############### Solving Game with A*  Algorithm ############

--- Solved using A* in 0.0006482601165771484 seconds ---

Solution:   Right -> Right -> Down -> Right -> Right -> Right -> Down 
```
## References
Tahani Q. Alhassan, Shefaa S. Omar, Lamiaa A. Elrefaei,
Game of Bloxorz Solving Agent Using Informed and Uninformed Search Strategies,
Procedia Computer Science,
Volume 163,
2019,
Pages 391-399,
ISSN 1877-0509,
https://doi.org/10.1016/j.procs.2019.12.121.
(http://www.sciencedirect.com/science/article/pii/S187705091932160X)
Abstract: Bloxorz is a block sliding puzzle game that can be categorized as a pathfinding problem. Pathfinding problems are well known problems in Artificial Intelligence field. In this paper, we proposed a single agent implementation to solve level-1 of Bloxorz game using Informed and Uninformed searching algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), and A-star (A*) searching algorithms. The agent solves the problem using the three algorithms to compare their performance and conduct a conclusion that may help in improving the use of searching algorithms in this area. In this paper, A* and breadth-first search algorithms are founded to be more convenient to solve this problem.
Keywords: A*; agent; Bloxorz; breadth-first search; depth-first search; heuristic function; path-finding problem; puzzle


This code is available under MIT License. Please read the License file for more information and maintain the citation to the authors of the paper. 
Copyright (C) 2020 - Abhilshit Soni 

