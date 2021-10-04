'''
Definitions for GameNode, GameSearch and MCTS

Author: Tony Lindgren

Completed By: Maryam Askari and Mahtab BabaMohammadi
'''
from time import process_time
import random
import math


class GameNode:
    '''
    This class defines game nodes in game search trees. It keep track of: 
    state
    '''
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
        self.number_of_visit = 0
        self.node_wins = 0
        self.children = []      # A list of children
        self.untried_moves = self.state.actions()   # A list of all possible moves!

    def node_children(self):
        node = self.state.actions()
        self.untried_moves.remove(node)
        self.children.append(node)
        return node

    def win_visited(self, result):
        self.number_of_visit = 1 + self.number_of_visit
        self.node_wins = 1 + self.node_wins

    def ucb1_calculator(self):
        max_ucb = 0
        max_child = None
        for child in self.state.children:
            ucb1 = child.node_wins / child.number_of_visit + 1.4 * math.sqrt(math.log(self.state.number_of_visit) / child.number_of_visit)
            if ucb1 > max_ucb:
                max_child = child
                max_ucb = ucb1
        return max_child
           
class GameSearch:
    '''
    Class containing different game search algorithms, call it with a defined game/node
    '''                 
    def __init__(self, game, depth=3, time=None):
        self.state = game       
        self.depth = depth
        self.time = time

    def mcts(self):                     
        start_time = process_time() 
        tree = GameNode(self.state)
        tree.actions_left = tree.state.actions()    # A list of possible actions from four_in_a_row
        elapsed_time = 0
        while elapsed_time < self.time:   
            leaf = self.select(tree)
            child = self.expand(leaf)               
            result = self.simulate(child) 
            self.back_propagate(result, child)         
            stop_time = process_time()
            elapsed_time = stop_time - start_time
        move = self.actions(tree)
        return move

    def select(self, tree: GameNode):
        if len(tree.untried_moves) == 0 and len(tree.children)!=0:
            move = tree.state.actions()
            random.shuffle(move)
            node = move.ucb1_calculator()
            return self.select(node)
        return tree.node


    def expand(self, leaf: GameNode):
        if leaf.untried_moves != 0:
            move = random.shuffle(leaf.untried_moves)
            leaf = leaf.state.result(move)
        return leaf

    def simulate(self, child: GameNode):
        invert_reward = True
        while True:
            if node.is_terminal():
                terminal,reward = child.state.is_teminal()
                return 1 - reward if invert_reward else reward
            node = node.find_random_child()
            invert_reward = not invert_reward

    def back_propagate(self, result: GameNode, child: GameNode):
        if self.state.parent is None:
            return
        else:
           return result.state.parent.back_propagate(result)


    def actions(self, tree: GameNode):
        if len(tree.untried_moves):
            move = tree.state.actions()
            random.shuffle(move)
            new_state = tree.state.result(move)
            return new_state




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