import TicTacToe as TTT

t = TTT.TicTacToe()
inputStr = "1"
print("Initial board is shown on the right:")
t.print()
while inputStr != "0":
    if t.turn % 2 == 0:
        player = "O"
    else:
        player = "X"
    print("Player " + player + "'s turn.")
    inputStr = input("Enter a Number from 1 to 9 to play, 0 to exit: ")
    try:
        int(inputStr)
    except ValueError:
        print("Input is not an integer!")
        continue
    if int(inputStr) < 0 or int(inputStr) > 9:
        print("Input is not valid!")
        continue
    if int(inputStr) == 0: break
    t.draw(int(inputStr), player)
    print("Current board is shown on the right:")
    t.print()
    gameStat = t.hasAWinner()
    if gameStat == "O" or gameStat == "X":
        print("Player " + gameStat + " is the winner!")
        break
    elif gameStat == "tie":
        print("It is a tie.")
        break
    else: continue
