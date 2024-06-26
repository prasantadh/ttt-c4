board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

player = 'X'
def swapplayer():
    if player == 'X':
        return 'O'

    if player == 'O':
        return 'X'

def checkwinner():
    if (board[x][0] == board[x][1] == board[x][2] ==player):
        return True

    if (board[0][y] == board[1][y] == board[2][y] == player):
        return True

    if (board[2][0] == board[1][1] == board[0][2] == player):
        return True

    return False

def printboard():
    print()
    print(f'  | 0 | 1 | 2')
    print('0 | {} | {} | {} '.format(board[0][0], board[0][1], board[0][2] ))
    print('1 | {} | {} | {} '.format(board[1][0], board[1][1], board[1][2] ))
    print('2 | {} | {} | {} '.format(board[2][0], board[2][1], board[2][2] ))

choice = 'y'
while choice == 'y':
    printboard()
    print("Current player: ", player)
    while True:
        x = int(input("enter row: "))
        y = int(input("enter col: "))
        if not (0 <= x <= 2):
            print("invalid value for x!")
            continue

        if board[x][y] == ' ':
            board[x][y] = player
            break
        print("invalid position!")

    if checkwinner() == True:
        printboard()
        board.clear()

        board = [
                    [' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']
                ]

        print(player, " WON!")
        choice = input("enter y to play: ")
    player = swapplayer()
