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

state0 = FourInARow('human', 'w')
state0 = state0.result(0)
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
state0 = state0.result(0)
"""state0 = state0.result(0)
state0 = state0.result(1)
state0 = state0.result(2)
state0 = state0.result(3)
state0 = state0.result(4)"""

print(state0.board)
print(state0.actions())
print(state0.pretty_print())
print(len(state0.board[2]))
#print(state0.is_terminal())