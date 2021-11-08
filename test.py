# =============================================================================
# Created By : Maryam Askari
# Date: 9/29/2021
# Time: 9:17 PM
# =============================================================================
"""The Module Has Been Build for..."""
# =============================================================================
# Imports
# =============================================================================
from four_in_a_row import FourInARow
from game_node_and_game_search import GameNode,GameSearch

state0 = FourInARow('human', 'w')
"""state0 = state0.result(0)
state0 = state0.result(0)
state0 = state0.result(0)
state0 = state0.result(1)
state0 = state0.result(1)
state0 = state0.result(1)
state0 = state0.result(2)
state0 = state0.result(2)
state0 = state0.result(2)
state0 = state0.result(3)
state0 = state0.result(3)
state0 = state0.result(0)"""

state0 = state0.result(1)

"""print(state0.board)
print(state0.actions())
print(state0.pretty_print())
print(len(state0.board[2]))
print(state0.is_terminal())"""

node = GameNode(state0)
_, node.node_wins=node.state.is_terminal()
max_ucb1 = tuple()
for i in node.node_children():
    _, i.node_wins= i.state.is_terminal()
    node.number_of_visit += 1
    i.number_of_visit +=1
    print("win", i.node_wins)
    print(i.state.board)
    print("number visit",i.number_of_visit)
    print("number visit _ parent",node.number_of_visit)
    print(i.ucb1_calculator())
    if 0 < i.ucb1_calculator():
        max_ucb1= (i, i.ucb1_calculator())
print('****************************')
state1 = state0.result(max_ucb1[0].action)
state0 = state0.result(1)
print(max_ucb1[0].action)
node = GameNode(state1)
_, node.node_wins=node.state.is_terminal()
max_ucb1 = tuple()
for i in node.node_children():
    _, i.node_wins= i.state.is_terminal()
    node.number_of_visit += 1
    i.number_of_visit +=1
    print("win", i.node_wins)
    print(i.state.board)
    print("number visit", i.number_of_visit)
    print("number visit _ parent",node.number_of_visit)
    print(i.ucb1_calculator())
    if 0 < i.ucb1_calculator():
        max_ucb1= (i, i.ucb1_calculator())
print('****************************')
state1 = state0.result(max_ucb1[0].action)
state0 = state0.result(1)
print(max_ucb1[0].action)
node = GameNode(state1)
_, node.node_wins=node.state.is_terminal()
max_ucb1 = tuple
for i in node.node_children():
    _, i.node_wins= i.state.is_terminal()
    node.number_of_visit += 1
    i.number_of_visit +=1
    print("win", i.node_wins)
    print(i.state.board)
    print("number visit",i.number_of_visit)
    print("number visit _ parent",node.number_of_visit)
    print(i.ucb1_calculator())
    if 0 < i.ucb1_calculator():
        max_ucb1= (i, i.ucb1_calculator())
print('****************************')
state1 = state0.result(max_ucb1[0].action)
state0 = state0.result(1)
print(max_ucb1[0].action)
node = GameNode(state1)
_, node.node_wins=node.state.is_terminal()
max_ucb1 = tuple
for i in node.node_children():
    _, i.node_wins= i.state.is_terminal()
    node.number_of_visit += 1
    i.number_of_visit +=1
    print("win", i.node_wins)
    print(i.state.board)
    print("number visit",i.number_of_visit)
    print("number visit _ parent",node.number_of_visit)
    print(i.ucb1_calculator())
    if 0 < i.ucb1_calculator():
        max_ucb1= (i, i.ucb1_calculator())

"""from subprocess import Popen, PIPE, STDOUT

p = Popen('C:\Program Files\SICStus Prolog VC16 4.6.0\\bin\sicstus', shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
cmd = open('D:\prolog\demo.pl').read()
res = p.communicate(cmd)
for line in res:
    print line"""
