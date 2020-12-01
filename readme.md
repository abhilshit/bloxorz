## Bloxorz Game!

Bloxorz is a 3-D block sliding puzzle game consists of a terrain that is built
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
shown 
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
Steps to run

  E.g.
```bash
python game.py
```
Import project in pycharm and run game.py

> **Note**: level-1 of Bloxorz game is implemented using A* algorithm to find fast and Optimal solution.

## OutPut
- List of steps performed to reach the gaol in text file
- Screenshot of outputs 

>**Note**: .