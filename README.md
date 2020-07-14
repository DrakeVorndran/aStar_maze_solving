
# A* implemented in python
This project implements the a* pathfinding algorithm in python  
For more information on the A* algorithm, please look [here](https://www.geeksforgeeks.org/a-search-algorithm)

## Maze Class
This is a class that represents the maze with a start, an end, and walls.  
Walls fill a cell and make it impossible to pass-through.
#### Repersentation
The maze is represented as a 2d array, with 0's being spaces you can pass through, and 1's being walls.
Each cell is addressed as a tuple containing 2 values, the x and y coordinate of the cell, indexed at 0, starting from the top left corner. (I.E. `(0,0)` would be the top left corner)

the constructor for this class takes many parameters, but most of them have default values.
#### Parameters:
| Parameter | default | explanation | 
|--|--| -- |
| height | `10` | the height of the maze |
| width | `10` | the width of the maze |
| walls | empty array | a list of tuples containing the location tuples of a wall |
| start | `(0,0)` | the position you are meant to start the maze, as a location tuple |
| end | bottom right corner | the position you are meant to win the maze, as a location tuple |
#### Heuristics:
There are 3 heuristics that you can use
0 - Euclidean Distance
1 - Diagonal Distance
2 -  Manhattan Distance

For more information, please look [here](https://www.geeksforgeeks.org/a-search-algorithm)
#### Definition:
```python
def  __init__(self, height=10, width=10, walls=[], start=(0,0), end=None):
```

#### Methods:
The only method is one for representing the maze as a string, if you print the maze object, it will look nice.

## a_star Function
The a_star function is the function that actually solves the maze, and returns a list of location tuples in the order that the maze can be solved in.
#### Parameters:
| Parameter | default | explanation | 
|--|--|--|
| maze | N/A | A maze object that will be solved |
| v | `False` | print a representation of the maze at every step |
| h_type | `0` | a selector for the heuristic that calculates the distance between the end and the current cell |
#### Definition:
```python
def  a_star(maze, v=False, h_type=0):
```

