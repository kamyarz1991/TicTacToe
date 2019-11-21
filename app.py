# tic tac toe game
import sys
from random import seed
from random import randint


def winnerChecker(a):
    winner = ''
    for i in range(0, 3):
        if a[i] == a[i+3] == a[i+6] != ' ':
            winner = a[i]
            break

    for j in range(0, 9, 3):
        if a[j] == a[j+1] == a[j+2] != ' ':
            winner = a[j]
            break

    if a[0] == a[4] == a[8] != ' ' or a[2] == a[4] == a[6] != ' ':
        winner = a[4]

    return winner


def printBoard(board):

    for i in range(0, 9):
        if i % 3 == 0 or i % 3 == 1:
            sys.stdout.write(board[i] + '|')
        if i % 3 == 2:
            sys.stdout.write(board[i]+'\n-+-+-\n')


def playGame(board):
    PLAYER_1 = "O"
    PLAYER_2 = "X"
    coin = randint(1, 2)

    if coin == 1:
        turn = PLAYER_1
    else:
        turn = PLAYER_2

    Flag = True
    while Flag:
        print("It is your turn PLAYER who plays " + turn)
        val = int(input("Enter a number between 1 and 9: "))
        if val >= 1 and val <= 9:
            if board[val-1] == ' ':
                if turn == PLAYER_1:
                    board[val-1] = turn
                    turn = PLAYER_2
                else:
                    board[val-1] = turn
                    turn = PLAYER_1
            else:
                print(
                    "The position you want to play is 69... Just kidding its already filled")
        else:
            print("Dude seriously... cant you see 1 and 9 in there... oh my go00000d")

        printBoard(board)
        winner = winnerChecker(board)
        print(winner)
        if winner == '':
            for i in range(0, 9):
                if (board[i] == ' '):
                    Flag = True
                    break
                else:
                    Flag = False
            if Flag == False:
                print("It is a Tie... you both are loosers")
        else:
            print("we have a winner and it is " + winner)
            Flag = False
    Play_Again()


def Play_Again():

    Play_Again = input(
        "Do you want to play again???, Please dont be a dick and enter y or n: ")
    if Play_Again == "y":
        New_Board = [' ']*9
        printBoard(New_Board)
        playGame(New_Board)
    elif Play_Again == "n":
        print("Okay go ahead, leave me here you jerk")
    else:
        print("I told you dont be a dick maaan, OH my gooooood")


The_Board = [' ']*9
printBoard(The_Board)

playGame(The_Board)
