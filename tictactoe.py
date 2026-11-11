def displayBoard(board):
    print(' ═════' * 3)
    print(f'║  {board[0]}  ║  {board[1]}  ║  {board[2]}  ║')
    print(' ═════' * 3)
    print(f'║  {board[3]}  ║  {board[4]}  ║  {board[5]}  ║')
    print(' ═════' * 3)
    print(f'║  {board[6]}  ║  {board[7]}  ║  {board[8]}  ║')
    print(' ═════' * 3)

def checkWin(board, winningBoards) -> str:
    for a, b, c in winningBoards:
        if board[a] == board[b] == board[c]:
            return board[a]

def returnPlayer(turn, playerSymbols) -> str:
    if turn % 2 == 0:
        return playerSymbols.get(turn % 2, 'X')
    else:
        return playerSymbols.get(turn % 2, 'O')

def returnTie(occupied) -> bool:
    if len(occupied) == 9:
        return True
    return False

def customPlayerSymbols() -> dict:
    return {k: v for k in range(2) if len((v := input(f'Enter custom symbol, Player {k + 1}\n> '))) == 1}

def main():

    playerSymbols = customPlayerSymbols()

    turn = 0

    board = [str(x) for x in range(1, 10, 1)]

    occupied = set()

    winningBoards = (
            # horizontal
            (0,1,2), (3,4,5), (6,7,8),
            # vertical
            (0,3,6), (1,4,7), (2,5,8),
            # diagonal
            (0,4,8), (2,4,6)
            )

    print('''

A player wins when they mark all three spaces of a row, column, or diagonal of the grid.

Type 'q' to quit.
''')
    print()
    while True:
        cPlayer = returnPlayer(turn, playerSymbols)
        turn += 1
        print('Turn: ', turn)
        print(f'{cPlayer}, 1-9')
        displayBoard(board)
        print('\n')
        choice = input('> ')

        if choice.isdigit() and 0 < int(choice) < 10:
            if choice not in occupied:
                board[int(choice) - 1] = cPlayer
                occupied.add(choice)
                if checkWin(board, winningBoards) == cPlayer:
                    print('Turn: ', turn + 1)
                    print(f'Player {cPlayer} wins!')
                    displayBoard(board)
                    break
                elif returnTie(occupied) == True:
                    print('Turn: ', turn + 1)
                    print("It's a tie.")
                    displayBoard(board)
                    break
                else: continue
            else:
                print(f'Square {choice} occupied with {board[int(choice) - 1]}')
                turn -= 1

        elif choice == 'q':
            break

        else:
            print('Invalid answer.')
            turn -= 1





if __name__=='__main__':
    main()
