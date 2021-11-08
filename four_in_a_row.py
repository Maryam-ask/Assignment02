'''
Four in a row

Author: Tony Lindgren

Completed By: Maryam Askari and Mahtab BabaMohammadi
'''
from copy import deepcopy


class FourInARow:
    def __init__(self, player, chip):
        new_board = []
        for _ in range(7):
            new_board.append([])
        self.board = new_board
        self.action = list(range(7))
        if chip != 'r' and chip != 'w':
            print('The provided value is not a valid chip (must be, r or w): ', chip)
        if player == 'human' and chip == 'w':
            self.ai_player = 'r'
        else:
            self.ai_player = 'w'
        self.curr_move = chip

    def to_move(self):
        return self.curr_move

    # actions
    def actions(self):
        """
        A method to search for all possible action
        :return: A list of all columns which has empty row
        """
        actions = []
        for c in range(len(self.board)):
            if len(self.board[c]) < 6:
                actions.append(c)
        return actions

    def result(self, action):
        dc = deepcopy(self)
        if self.to_move() == 'w':
            dc.curr_move = 'r'
            dc.board[action].append(self.to_move())
        else:
            dc.curr_move = 'w'
            dc.board[action].append(self.to_move())
        return dc

    def eval(self):
        center = self.board[3][3]


    def is_terminal(self):
        # check vertical
        for c in range(0, len(self.board)):  # Columns
            count = 0
            curr_chip = None
            for r in range(0, len(self.board[c])):  # Rows
                if curr_chip == self.board[c][r]:
                    count = count + 1
                else:
                    curr_chip = self.board[c][r]
                    count = 1
                if count == 4:
                    if self.ai_player == curr_chip:
                        #print('Found vertical win')
                        return True, 100  # MAX ai wins positive utility
                    else:
                        #print('Found vertical loss')
                        return True, -100  # MIN player wins negative utility

        # check horizontal
        curr_col = 0
        for r in range(6):      # rows
            count = 0
            curr_chip = None
            for c in range(0, len(self.board)):  # Columns should increase!
                if r < len(self.board[c]):
                    if curr_chip == self.board[c][r] and curr_col+1 == c:
                        count = count + 1
                    else:
                        curr_chip = self.board[c][r]
                        count = 1
                    curr_col = c
                    if count == 4:
                        if self.ai_player == curr_chip:
                            #print('Found horizontal win')
                            return True, 100  # MAX ai wins positive utility
                        else:
                            #print('Found horizontal loss')
                            return True, -100

        # check positive diagonal
        for c in range(7 - 3):
            for r in range(6 - 3):
                if len(self.board[c]) > r and len(self.board[c + 1]) > r + 1 and len(self.board[c + 2]) > r + 2 and len(
                        self.board[c + 3]) > r + 3:
                    if self.ai_player == self.board[c][r] and self.ai_player == self.board[c + 1][
                        r + 1] and self.ai_player == self.board[c + 2][r + 2] and self.ai_player == self.board[c + 3][
                        r + 3]:
                        #print('Found positive diagonal win')
                        return True, 100
                    elif self.ai_player != self.board[c][r] and self.ai_player != self.board[c + 1][
                        r + 1] and self.ai_player != self.board[c + 2][r + 2] and self.ai_player != self.board[c + 3][
                        r + 3]:
                        #print('Found positive diagonal loss')
                        return True, -100

        # check negative diagonal
        for c in range(7 - 3):
            for r in range(6 - 3, 6):
                if len(self.board[c]) > r and len(self.board[c + 1]) > r - 1 and len(self.board[c + 2]) > r - 2 and len(
                        self.board[c + 3]) > r - 3:
                    if self.ai_player == self.board[c][r] and self.ai_player == self.board[c + 1][
                        r - 1] and self.ai_player == self.board[c + 2][r - 2] and self.ai_player == self.board[c + 3][
                        r - 3]:
                        #print('Found negative diagonal win')
                        return True, 100
                    elif self.ai_player != self.board[c][r] and self.ai_player != self.board[c + 1][
                        r - 1] and self.ai_player != self.board[c + 2][r - 2] and self.ai_player != self.board[c + 3][
                        r - 3]:
                        #print('Found negative diagonal loss')
                        return True, -100

        # check draw
        """check_rows = 0
        for c in range(len(self.board)):
            if len(self.board[c]) == 6:
                check_rows += 1
        if check_rows == 6:
            return True, 0"""
        if not self.actions():  # if there is NO place to move
            print("Nothing found, Draw!")
            return True, 0

        return False, 0


        # pretty_print
    def pretty_print(self):
        """
        A method to print out the board.
        """
        board_copy = deepcopy(self.board)

        for c in range(len(board_copy)):
            if len(board_copy[c]) != 6:
                for _ in range(6 - len(board_copy[c])):
                    board_copy[c].append("_")

        for i in range(7):
            print(i+1, "", end="")
        print()
        for r in range(5, -1, -1):
            for c in range(7):
                print(board_copy[c][r], end=" ")
            print()


