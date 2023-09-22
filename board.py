class Board:
    def __init__ (self, board):
        self.__board = board

    def print(self):
        for i in range(9):
            if i == 0 or i == 3 or i == 6:
                print('-------------------------')  # Print top boarders
            for j in range(9):
                if j == 0 or j == 3 or j == 6:
                    print ('| ', end='')
                if j == 8:  # If last num in row, do not print space after
                    if self.board[i][j] == None:  # If val is empty
                        print(' ', end=' |')
                    else:  # If val is num
                        print(self.board[i][j], end=' |')
                else:
                    if self.board[i][j] == None:  # If val is empty
                        print(' ', end=' ')
                    else:  # If val is num
                        print(self.board[i][j], end=' ')
            print()  # Print new line if end of row
        print('-------------------------')  # Print bottom boarder
    