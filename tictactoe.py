### tictactoe.py ###
# best game ever

import os




# turn logic based on 0 and 1 for X O
def checkPlayerTurn(turn) -> str:
    # uneven numbers are plr 2, even nums plr 1
    if turn % 2 == 0:
        return "X"
    else:
        return "O"


# function to easily display board for all loops and purposes
def displayBoard(board):
    print(' --- --- --- ')
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print(' --- --- --- ')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print(' --- --- --- ')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')
    print(' --- --- --- ')


# checks if there is a winner with sequence unpacking
def checkWin(board, winningBoards):
    for a, b, c in winningBoards:
        if board[a] == board[b] == board[c]:
            return board[a]
    return None


# main function
def main():

    # turn decides player increments per turn
    turn = 0

    # the actual game board
    board = ['1','2', '3', '4', '5', '6', '7', '8', '9']

    # the list of sets to compare board to
    winningBoards = [
            (0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (0,4,8),
            (2,4,6)
            ]

    # for the game loop
    running = True

    # for keeping track of filled squares
    occupied = set()


    # game loop
    while True:
        #display board
        displayBoard(board)
        # have player variable
        currentPlr = checkPlayerTurn(turn)
        print(f"{currentPlr}, 1-9")
        # current plr input
        answer = input('> ')

        # quit game loop
        if answer == 'q':
            break
        # True if 0-9 ans value only
        if answer.isdigit():
            # ans - 1 because 1 would be 2 in a list
            if int(answer) - 1 > -1 and int(answer) - 1 < 9:
                # check if board already occupied there
                if int(answer) - 1 not in occupied:
                    answer = int(answer)
                    # place symbol of playrr on board
                    board[answer - 1] = currentPlr
                    # add turn for turn logic
                    turn += 1
                    # add ans to occupied
                    occupied.add(answer - 1)
                    # if there is a winner
                    if checkWin(board, winningBoards) != None:
                        print(f"Player {checkWin(board, winningBoards)} Wins!")
                        break
                    # all squares are occupied means tie
                    if len(occupied) == 9:
                        print("It's a tie.")
                        break
                
                # ans already in occupied set
                else:
                    print("Already filled.")

            # ans is a digit but out of range
            else:
                print(f"{answer} is out of range.")
        # ans is not even a digit
        else:
            print(f"{answer} is not a valid input")

        print('\n' * 5)

if __name__=='__main__':
    main()
