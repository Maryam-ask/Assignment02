'''
Definitions for GameNode, GameSearch and MCTS

Author: Tony Lindgren

Completed By: Maryam Askari and Mahtab BabaMohammadi
'''
from time import process_time
import random
import math
from four_in_a_row import FourInARow

class GameNode:
    '''
    This class defines game nodes in game search trees. It keep track of: 
    state
    '''
    def __init__(self, state, node=None):
        self.state = state
        self.node = node
        self.number_of_visit = 0
        self.vi = 0
        self.ucb1 = 100000
        self.node = node
           
class GameSearch:
    '''
    Class containing different game search algorithms, call it with a defined game/node
    '''                 
    def __init__(self, game, depth=3):
        self.state = game       
        self.depth = depth
        self.time = 0

    def mcts(self):
        start_time = process_time()
        root = self.state
        # print(root)
        tree = GameNode(self.state)
        tree.actions_left = tree.state.actions()   
        elapsed_time = 0
        while elapsed_time < self.time:   
            leaf = self.select(tree, root)
            # child = self.expand(leaf)
            result = self.simulate(leaf)
            self.back_propagate(result, leaf)
            stop_time = process_time()
            elapsed_time = stop_time - start_time
        move = self.actions(tree)
        return move

    def select(self, tree, root):
        stop, value = root.is_terminal()
        if stop:
            return root
        else:
            children = root.actions()
            max_ucb1 = -100000
            max_child = None
            for child in children:
                if self.ucb1_calculator(child) > max_ucb1:
                    max_ucb1 = self.ucb1_calculator(child)
                    max_child = child
            self.select(tree, max_child)


    def expand(self, leaf):
        pass

    def simulate(self, si):
        while True:
            terminal, value = si.state.is_terminal()
            if terminal:
                return si.vi
            actions = si.state.actions()
            random.shuffle(actions)
            si = si.state.result(actions[0])

    def back_propagate(self, result, si):
        si.vi += result
        si.number_of_visit += 1
        while si.node:
            si.node.vi = result
            si.node.number_of_visit += 1
            si = si.node

    def actions(self, tree):
        return  tree

    def ucb1_calculator(self, si):
        si.ucb1 = si.vi + 2 * math.sqrt(math.log2(si.node.number_of_visit)/si.number_of_visit)
        return si.vi

    def minimax_search(self): 
        start_time = process_time()   
        _, move = self.max_value(self.state, self.depth)
        return move
    
    def max_value(self, state, depth):
        move = None
        terminal, value = state.is_terminal()
        if terminal or depth == 0:
            return value, None
        v = -100000
        actions = state.actions()
        random.shuffle(actions)
        for action in actions:
            new_state = state.result(action)
            v2, _ = self.min_value(new_state, depth - 1)
            if v2 > v:
                move = action
                v = v2
        return v, move
    
    def min_value(self, state, depth):
        move = None
        terminal, value = state.is_terminal()
        if terminal or depth == 0:
            return value, None  
        v = 100000
        actions = state.actions()
        random.shuffle(actions)
        for action in actions:
            new_state = state.result(action)
            v2, _ = self.max_value(new_state, depth - 1)
            if v2 < v:
                move = action
                v = v2
        return v, move

    def alpha_beta_search(self):
        start_time = process_time()
        _, move = self.alpha_value(self.state, self.depth, a=-math.inf, b=+math.inf)
        return move

    def alpha_value(self, state, depth, a=-math.inf, b=+math.inf):
        move = None
        terminal, value = state.is_terminal()
        if terminal or depth == 0:
            return value, None
        v = -math.inf
        actions = state.actions()
        random.shuffle(actions)
        for action in actions:
            new_state = state.result(action)
            v2, _ = self.beta_value(new_state, depth - 1, a=-math.inf, b=+math.inf)
            if v2 > v:
                v = v2
                move = action
                a = max(a, v)
            if v >= b:
                return v, move
            return v, move

    def beta_value(self, state, depth, a=-math.inf, b=+math.inf):
        move = None
        terminal, value = state.is_terminal()
        if terminal or depth == 0:
            return value, None
        v = +math.inf
        actions = state.actions()
        random.shuffle(actions)
        for action in actions:
            new_state = state.result(action)
            v2, _ = self.alpha_value(new_state, depth - 1, a=-math.inf, b=+math.inf)
            if v2 < v:
                v = v2
                move = action
                b = min(b, v)
            if v >= b:
                return v, move
            return v, move