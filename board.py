class Board:
    def __init__ (self, board):
        self.board = board

    def print(self):
        for i in range(9):
            for j in range(9):
                if i == 8:  # If last num in row, do not print space after
                    if self.board[i][j] == None:  # If val is empty
                        print(' ', end='')
                    else:  # If val is num
                        print(self.board[i][j], end='')
                else:
                    if self.board[i][j] == None:  # If val is empty
                        print(' ', end=' ')
                    else:  # If val is num
                        print(self.board[i][j], end=' ')
            print()  # Print new lin if end of row