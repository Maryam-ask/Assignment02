'''
Define game and start execution of game search

Author: Tony Lindgren

Completed By: Maryam Askari and Mahtab BabaMohammadi
'''
from four_in_a_row import FourInARow
from game_node_and_game_search import GameSearch

    
def ask_ai(state0):
    gs = GameSearch(state0, depth=3)
    '''MinMax_search'''
    # move = gs.minimax_search()
    '''Alpha_beta_search'''
    # move = gs.alpha_beta_search()
    # gs = GameSearch(state0, depth=3, time=20)
    '''mct Search'''
    move = gs.mcts()
    state1 = state0.result(move)
    print('--------')
    print('AI moves')
    print('--------')
    state1.pretty_print()  
    stop, value = state1.is_terminal() 
    if stop == True:
        if value > 0:
            print('AI won')                       
        else:
            print('Human won')
        return state1, True
    return state1, False

def ask_player(state0):
    """
    A Method to get the input from the user.
    :param state0:
    :return: returns the satate and result of is_terminal() method
    """
    move = int(input("Enter you column to move.(1-7)")) - 1

    while move >= 7 or move < 0:
        print("[Error] Try Again!")
        move = int(input("Enter you column to move.(1-7)"))-1

    state1 = state0.result(move)
    print("------------")
    print("Player moves")
    print("------------")
    state1.pretty_print()
    stop, value = state1.is_terminal()
    if stop == True:
        if value > 0:
            print("AI won")
        else:
            print("Human won")
        return state1, True
    return state1, False

def main():
    print('Welcome to play for-in-a-row!')
    answer = None
    while answer != 'y' and answer != 'n':
        answer = input('Would you like to start [y/n]: ')
    if answer == 'y':
        state0 = FourInARow('human', 'w')
        stop = False
        while not stop:
        #Ask player         
            state1, stop1 = ask_player(state0)
            if stop1:
                break
            else:
        #AI move
                state0, stop2 = ask_ai(state1)  
                if stop2:
                    break                
    else:
        state0 = FourInARow('ai', 'w')
        stop = False
        while not stop: 
        #AI move
            state1, stop1 = ask_ai(state0)    
            if stop1:
                break
            else:  
        #Ask player
                state0, stop2 = ask_player(state1)    
                if stop2:
                    break               
       
if __name__ == "__main__":
    main()