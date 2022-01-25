# 没有类型提示的maze代码
from enum import Enum
# from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from generic_search import dfs, node_to_path, Node, bfs# , astar
from collections import namedtuple

class Cell:
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

# 重要！
# 这里使用的namedtuple是个关键，如果直接定义class，不对其__eq__方法进行重定义
# 那么在dfs里的explored进行查找的时候，永远无法在里面找到记录过得数据，导致循环一直会进行下去
MazeLoaction = namedtuple('MazeLoaction',['row', 'column'])


class Maze:
    def __init__(self, rows = 10, columns = 10, sparseness = 0.2, start = MazeLoaction(0, 0), goal = MazeLoaction(9, 9)):
    # initialize basic instance variables
        self._rows = rows
        self._columns = columns
        self.start= start
        self.goal = goal
        self._grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
    # populate the grid with blocked cells
        self._randomly_fill(rows, columns, sparseness)
    # fill the start and goal locations in
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows, columns, sparseness):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    # return a nicely formatted version of the maze for printing
    def __str__(self) :
        output = ""
        for row in self._grid:
            output +="".join([c for c in row]) + "\n"
        return output

    def goal_test(self, ml) :
        return ml == self.goal

    def successors(self, ml) :
        locations= []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLoaction(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row-1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLoaction(ml.row - 1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLoaction(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLoaction(ml.row, ml.column - 1))
        return locations

    def mark(self, path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL



if __name__ == '__main__':
    # Test DFS
    m = Maze()
    print(m)
    solution1 = dfs(m.start, m.goal_test, m.successors)
    if solution1 is None:
        print('No solution found using depth-first search!')
    else:
        path1 = node_to_path(solution1)
        m.mark(path1)
        print(m)
        m.clear(path1)
    # Test BFS
    solution2 = bfs(m.start, m.goal_test, m.successors)
    if solution2 is None:
        print('No solution found using breadth-first search!')
    else:
        path2 = node_to_path(solution2)
        m.mark(path2)
        print(m)
        m.clear(path2)
