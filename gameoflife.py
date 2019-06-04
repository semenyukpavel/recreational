import time

def printBoard():
    for i in range(n):
        s = str()
        for j in range(n):
            s+=board[i][j]
            s+= ' '
        print(s)

def continueGame():
    c = str(input("Y for another game, else for quit: "))
    if c!='Y':
        gameOn = False
        return gameOn

def printRules():
    print("Welcome to Conway's Game of Life Python Edition!")
    print("Simple rules:")
    print("1. The board is NxN, where N is the number you enter on the next screen")
    print("2. Then you enter the initial board setup")
    print("It should consist of '.' -- dead cells and 'X' -- live cells")
    print("After that the Game begins. You can advance the cycle by pressing any latin character")
    print("If you print anything else, the cycle stops")
    print("Enjoy!")

gameOn = True        
while(gameOn):
    n = int(input("Enter board dimensions:"))
    board = []
    row = []
    printRules()
    for i in range(n):
        for j in range(n):
            row.append('.')
        board.append(row)
    printBoard()
    print("Enter initial setup:\n")
    for i in range(n):
        for j in range(n):
            board[i][j] = input().split(' ')
    gameOn = continueGame()
print("Thanks for playing!")
        
