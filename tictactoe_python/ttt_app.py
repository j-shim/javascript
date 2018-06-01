import TicTacToe as TTT

t = TTT.TicTacToe()
inputStr = "1"
print("Initial board is:")
t.print()
while inputStr != "0":
    if t.turn % 2 == 0:
        player = "O"
    else:
        player = "X"
    print("Player " + player + "'s turn.")
    inputStr = input("Enter a Number from 1 to 9: ")
    if inputStr == "0": break
    t.draw(int(inputStr), player)
    print("Current board is:")
    t.print()
    gameStat = t.hasAWinner()
    if gameStat == "O" or gameStat == "X":
        print("Player " + gameStat + " is the winner!")
        break
    elif gameStat == "tie":
        print("It is a tie.")
        break
    else: continue
