class TicTacToe:
    def __init__(this):
        this.board = [
            ["*", "*", "*"],
            ["*", "*", "*"],
            ["*", "*", "*"] 
        ]
        this.turn = 0 # Player O plays first (0 to 8)

    def draw(this, num, player):
        x = (num - 1) // 3 # Floor division by 3 to get x-coordinate for 3x3
        y = (num - 1) % 3 # y-coordinate
        if this.board[x][y] == "*":
            this.board[x][y] = player
            this.turn += 1
            return True
        else:
            print("You can't draw in that box!")
            return False

    def hasAWinner(this):
        for x in range(3):
            if this.checkRowColDiag("row", x, "O") == True:
                return "O"
            if this.checkRowColDiag("row", x, "X") == True:
                return "X"
            if this.checkRowColDiag("col", x, "O") == True:
                return "O"
            if this.checkRowColDiag("col", x, "X") == True:
                return "X"
        for x in range(2):
            if this.checkRowColDiag("diag", x, "O") == True:
                return "O"
            if this.checkRowColDiag("diag", x, "X") == True:
                return "X"
        if this.turn == 8:
            return "tie"
        else:
            return "not yet"

    def checkRowColDiag(this, spec, num, player):
        if spec == "row":
            for x in range(3):
                if this.board[num][x] != player: return False
            return True
        elif spec == "col":
            for x in range(3):
                if this.board[x][num] != player: return False
            return True
        elif spec == "diag" and num == 0:
            for x in range(3):
                if this.board[x][x] != player: return False
            return True
        elif spec == "diag" and num == 1:
            for x in range(3):
                if this.board[2 - x][x] != player: return False
            return True
        else:
            print("Row, column or diagonal Not Specified")
            return False

    def print(this):
        i = 1
        print("-----------------------------")
        for x in this.board:
            tmpStr = "|    " + str(i) + " " + str(i + 1) + " " + str(i + 2)
            tmpStr = tmpStr + "    |    "
            for y in x:
                tmpStr = tmpStr + y + " "
            tmpStr += "   |"
            print(tmpStr)
            i += 3
        print("-----------------------------")
