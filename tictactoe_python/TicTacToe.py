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
            return "true"
        else:
            print("You can't draw in that box!")
            return "false"

    def hasAWinner(this):
        for x in range(3):
            if this.checkRowColDiag("row", x, "O") == "true":
                return "O"
            if this.checkRowColDiag("row", x, "X") == "true":
                return "X"
            if this.checkRowColDiag("col", x, "O") == "true":
                return "O"
            if this.checkRowColDiag("col", x, "X") == "true":
                return "X"
        for x in range(2):
            if this.checkRowColDiag("diag", x, "O") == "true":
                return "O"
            if this.checkRowColDiag("diag", x, "X") == "true":
                return "X"
        if this.turn == 8:
            return "tie"
        else:
            return "not yet"

    def checkRowColDiag(this, spec, num, player):
        if spec == "row":
            for x in range(3):
                if this.board[num][x] != player: return "false"
            return "true"
        elif spec == "col":
            for x in range(3):
                if this.board[x][num] != player: return "false"
            return "true"
        elif spec == "diag" and num == 0:
            for x in range(3):
                if this.board[x][x] != player: return "false"
            return "true"
        elif spec == "diag" and num == 1:
            for x in range(3):
                if this.board[2 - x][x] != player: return "false"
            return "true"
        else:
            print("Row, column or diagonal Not Specified")
            return "false"

    def print(this):
        print("---------------")
        for x in this.board:
            tmpStr = "|    "
            for y in x:
                tmpStr = tmpStr + y + " "
            tmpStr += "   |"
            print(tmpStr)
        print("---------------")
