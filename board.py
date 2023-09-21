class Board:
    def __init__ (self, board):
        self.board = board

    def print(self):
        for i in range(9):
            for j in range(9):
                if i == 8:
                    print(self.board[i][j], end='')  # If last num in row, do not print space after
                else:
                    print(self.board[i][j], end=' ')  # If last num in row, print space after
            print()  # Print new lin if end of row