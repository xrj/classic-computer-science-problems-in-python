# 没有类型提示版的代码
# from __future__ import annotations
# from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict,\
    # Any, Optional
# from typing_extensions import Protocol
from heapq import heappush, heappop
from collections import  deque

# T = TypeVar('T')

def linear_contains(iterable, key) :
    for item in iterable:
        if item == key:
            return True
    return False

# C = TypeVar("C", bound = "Comparable")

class Comparable:
    def __eq__(self, other) :
        ...
    def __lt__(self, other) :
        ...
    def __gt__(self, other) :
        return (not self < other) and self != other
    def __le__(self, other) :
        return self < other or self == other
    def __ge__(self, other) :
        return not self < other

def binary_contains(sequence, key) :
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid -1
        else:
            return True
    return False

class Stack:
    def __init__(self) :
        self._container = []

    @property
    def empty(self):
        return not self._container # not is true for empty container

    def push(self, item):
        self._container.append(item)

    def pop(self) :
        return self._container.pop() # LIFO

    def __str__(self):
        return repr(self._container)

class Node:
    def __init__(self, state, parent, cost = 0.0, heuristic = 0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other) :
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __str__(self):
        return "row is %d, column is %d" %(self.state.row, self.state.column)


def dfs(initial, goal_test, successors) :
    # frontier is where we've yet to go
    frontier = Stack()
    frontier.push(Node(initial, None))
    # explored is where we've been
    # explored = {initial}
    explored = set()
    explored.add(initial)
    # keep going while there is more to explore
    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        # if we found the goal, we're done
        if goal_test(current_state):
            return current_node
        # check where we can go next and haven't explored
        for child in successors(current_state):
            if child in explored:  # skip children we already explored
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None  # went through everything and never found goal


def node_to_path(node) :
    path = [node.state]
    # work backwards form end to front
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path

class Queue():
    def __init__(self):
        self._container = deque()

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft() #FILO

    def __repr__(self):
        return repr(self._container)

def bfs(initial, goal_test, successors):
    # frontier is where we've yet to go
    frontier = Queue()
    frontier.push(Node(initial, None))
    # explored is where we've been
    explored = set()
    explored.add(initial)

    # keep going while there is more to explore
    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        # if we found the goal, we're done
        if goal_test(current_state):
            return current_node
        # check where we can go next and haven't explored
        for child in successors(current_state):
            if child in explored: # skip children we already explored
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None

if __name__ == "__main__":
    print(linear_contains([1, 5, 15, 15, 15, 15, 20], 5))  # True
    print(binary_contains(["a", "d", "e", "f", "z"], "f"))  # True
    print(binary_contains(["john", "mark", "ronald", "sarah"], "sheila"))  # False
