'''
Refactor of CellGrid.py
'''
import random
import importlib
import numpy as np

class CellGrid:
    '''
    CellGrid Object
    >>> grid = CellGrid(size = 20)
    >>> grid.size()
    20
    >>> grid.out_of_bounds(20)
    True
    >>> grid.out_of_bounds(19)
    False
    >>> grid.set_cell(5,5)
    >>> grid.state[5][5]
    1
    >>> sum(sum(np.array(grid.state)))
    1
    >>> grid.randomize()
    >>> sum(sum(np.array(grid.state))) > 50
    True
    >>> sum(sum(np.array(grid.state))) < 150
    True
    '''
    def __init__(self, state = None, size = 30):
        if state == None:
            self.state = [[0 for i in range(0, size)] for i in range(0, size)]
        else:
            self.state = state

    def randomize(self, prob = 0.25):
        self.state = [[ int(random.random() < prob) for i in range(0, self.size())] for i in range(0, self.size())]
    
    def size(self):
        return len(self.state)

    def set_cell(self, x, y, value = 1):
        if self.out_of_bounds(x) or self.out_of_bounds(y):
            raise ValueError('CellGrid.set_cell: One or more coordinates out of bounds.\nX:{} \nY:{} \nSize:{}'.format(x, y, self.size()))
        self.state[x][y] = value
    
    def out_of_bounds(self, coordinate):
        if coordinate < 0 or coordinate >= self.size():
            return True
        return False
    
    def advance(self, rule):
        new_state = [[0 for i in range(0, self.size())] for i in range(0, self.size())]
        for x in range(0, self.size() - 1):
            for y in range(0, self.size() - 1):
                new_state[x][y] = rule.run(self.state, x, y)
        self.state = new_state 


class Rule:
    '''
    Rule object for advancing a CellGrid
    param ruleset is a dictionary
    '''
    def __init__(self):
        pass

    def run(self, state, x, y):
        return 0
        
class ConwayRule(Rule):
    '''
        Conway's Rule
        Determine if a state is dead or alive based on number of living cells within it's
        direct neighbours.
        >>> grid = CellGrid(state = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        >>> rule = ConwayRule()
        >>> rule.run(grid.state, 0,0)
        0
        >>> rule.count_neighbours(grid.state, 1, 1)
        2
        >>> rule.run(grid.state, 1,1)
        1
        >>> rule.run(grid.state, 2,1)
        0
        >>> grid.set_cell(3,1)
        >>> rule.run(grid.state, 2,1)
        1
    '''
    def __init__(self, b = [3], s = [2, 3]):
        self.b = b
        self.s = s

    def run(self, state, x, y):
        n = self.count_neighbours(state, x, y)
        if (state[x][y] == 0) & (n in self.b):
            # new cell is born
            return 1
        if (state[x][y] == 1) & (n in self.s):
            # existing cell survives
            return 1
        # cell is dead otherwise
        return 0

    def count_neighbours(self, state, x, y):
        return np.array(state)[max(x-1,0):x+2,max(y-1,0):y+2].sum() - state[x][y]

class GridGame():
    '''

    '''
    def __init__(self, size = 100, ruleName = "Conway"):
        self.cellGrid = CellGrid(size = size)
        MyRule = getattr(importlib.import_module("module.submodule"), ruleName + "Rule")
        self.rule = MyRule()

    def start(self):
        self.cellGrid.randomize()
        #for t in range(1,1000):
        self.cellGrid.advance(self.rule)

    