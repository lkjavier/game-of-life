'''
Refactor of CellGrid.py
'''
import copy
import json
import time
import random




class CellGrid:
    '''
    CellGrid Object
    '''
    def __init__(self, state = None, size = 30):
         if state == None:
            self.state = [[0 for i in range(0, size)] for i in range(0, size)]
        else:
            self.state = state

    def randomize(self):
        n = 0
        while n < self.size()*self.size() / 4 :
            self.set_cell(random.randint(0, self.size() -1), random.randint(0,self.size() -1))
            n += 1
    
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
        new_state = [[0 for i in range(0, size)] for i in range(0, size)]
        for _, x : self.size():
            for _, y : self.size():
                new_state[x][y] = rule.run(self.state, x, y)
        self.state = new_state 


class Rule:
    '''
    Rule object for advancing a CellGrid
    param ruleset is a dictionary
    '''
    def __init__(self):
        self.rules
        pass

    def run(self, state, x, y):
        return 0
        
class ConwayRule(Rule):

    def run(self, state):
        return 1        

class GridGame():
    
    def __init__(self, size = 100, rulename = "Conway"):
        self.cellGrid = new CellGrid(size = size)
        self.rule = new ConwayRule()

    def start()
        cellGrid.randomize()
        for t in range(1,1000):
            cellGrid.advance(rule)

    