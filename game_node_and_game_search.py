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
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.number_of_visit = 0
        self.node_wins = 0
        self.untried_moves = self.state.actions()  # A list of all possible moves!
        self.children= []

    def node_children(self, children):
        children_ubc1 = {}
        for child in children:
            children_ubc1[child] = child.ucb1_calculator()
        return max(children_ubc1, key=children_ubc1.get)

    def most_visited(self, children):
        children_visit = {}
        for child in children:
            children_visit[child] = child.number_of_visit
            return max(children_visit, key=children_visit.get)

    def ucb1_calculator(self):
        ucb1 = self.node_wins / self.number_of_visit + math.sqrt(2) * math.sqrt(math.log(self.parent.number_of_visit) / self.number_of_visit)
        return ucb1
           
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

    def select(self, tree):
        """
        A Method which get the root node and from root node get all the children and calculate ucb1 for the all children
        and return the child which has greater value in ucb1
        :param tree: Getting the root node
        :return: the child node with greater ucb1
        """
        if tree.untried_moves == []:
            tree = tree.node_children(tree.children)
            return self.select(tree)
        return tree

    def expand(self, leaf):
        terminal, value = leaf.state.is_terminal()
        if not terminal:
            action = random.choice(leaf.untried_moves)
            leaf.untried_moves.remove(action)
            next_move = leaf.state.result(action)
            child_move = GameNode(next_move, leaf, action)
            leaf.children.append(child_move)
            return child_move
        return leaf


    def simulate(self, child):
        stop, value = child.state.is_terminal()
        while not stop:
            action = random.choice(child.state.actions())  #
            new_state = child.state.result(action)
            stop, value = new_state.is_terminal()

        if value == 0:
            return None
        if new_state.to_move() == 'r':
            winning_chip = 'w'
        else:
            winning_chip = 'r'
        return winning_chip


    def back_propagate(self, result, child):
        while child != None:
            if result == child.state.to_move():
                child.number_of_visit += 1
                child.node_wins += 1
            else:
                child.number_of_visit += 1
            child = child.parent

    def actions(self, tree):
        children = tree.children
        most_visited_node = tree.most_visited(children)
        return most_visited_node.untried_moves


    def minimax_search(self): 
        start_time = process_time()
        elapsed_time = 0
        while elapsed_time < self.time:
            _, move = self.max_value(self.state, self.depth)
            stop_time = process_time()
            elapsed_time = stop_time - start_time
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
        elapsed_time = 0
        while elapsed_time < self.time:
            _, move = self.alpha_value(self.state, self.depth, a=-math.inf, b=+math.inf)
            stop_time = process_time()
            elapsed_time = stop_time - start_time
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