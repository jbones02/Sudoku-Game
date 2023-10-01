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
                    if self.__board[i][j] == None:  # If val is empty
                        print('*', end=' |')
                    else:  # If val is num
                        print(self.__board[i][j], end=' |')
                else:
                    if self.__board[i][j] == None:  # If val is empty
                        print('*', end=' ')
                    else:  # If val is num
                        print(self.__board[i][j], end=' ')
            print()  # Print new line if end of row
        print('-------------------------')  # Print bottom boarder
    
    # Checks if cur num is valid in its row
    def __valid_in_row(self, num, row_of_num):
        cur_row = self.__board[row_of_num]  # Get row of num
        if cur_row.count(num) == 1:  # Check if num is found in cur_row once
            return True
        else:
            return False
        
    # Checks if cur num is valid in its col
    def __valid_in_col(self, num, col_of_num):
        cur_col = []
        for i in range(9):  # Get col of num
            cur_col.append(self.__board[i][col_of_num])
        if cur_col.count(num) == 1:  # Check if num is found in cur_col once
            return True
        else:
            return False
        
    # Checks if cur num is valid in its box
    def __valid_in_box(self, num, row_of_num, col_of_num):
        cur_box = []
        # Get box of num
        if (0 <= row_of_num <= 2) and (0 <= col_of_num <= 2):  # If in box 0
            cur_box = [self.__board[0][0], self.__board[0][1], self.__board[0][2],
                       self.__board[1][0], self.__board[1][1], self.__board[1][2],
                       self.__board[2][0], self.__board[2][1], self.__board[2][2]]
        elif ((0 <= row_of_num <= 2) and (3 <= col_of_num <= 5)):  # If in box 1
            cur_box = [self.__board[0][3], self.__board[0][4], self.__board[0][5],
                       self.__board[1][3], self.__board[1][4], self.__board[1][5],
                       self.__board[2][3], self.__board[2][4], self.__board[2][5]]
        elif ((0 <= row_of_num <= 2) and (6 <= col_of_num <= 8)):  # If in box 2
            cur_box = [self.__board[0][6], self.__board[0][7], self.__board[0][8],
                       self.__board[1][6], self.__board[1][7], self.__board[1][8],
                       self.__board[2][6], self.__board[2][7], self.__board[2][8]]
        elif ((3 <= row_of_num <= 5) and (0 <= col_of_num <= 2)):  # If in box 3
            cur_box = [self.__board[3][0], self.__board[3][1], self.__board[3][2],
                       self.__board[4][0], self.__board[4][1], self.__board[4][2],
                       self.__board[5][0], self.__board[5][1], self.__board[5][2]]
        elif ((3 <= row_of_num <= 5) and (3 <= col_of_num <= 5)):  # If in box 4
            cur_box = [self.__board[3][3], self.__board[3][4], self.__board[3][5],
                       self.__board[4][3], self.__board[4][4], self.__board[4][5],
                       self.__board[5][3], self.__board[5][4], self.__board[5][5]]
        elif ((3 <= row_of_num <= 5) and (6 <= col_of_num <= 8)):  # If in box 5
            cur_box = [self.__board[3][6], self.__board[3][7], self.__board[3][8],
                       self.__board[4][6], self.__board[4][7], self.__board[4][8],
                       self.__board[5][6], self.__board[5][7], self.__board[5][8]]
        elif ((6 <= row_of_num <= 8) and (0 <= col_of_num <= 2)):  # If in box 6
            cur_box = [self.__board[6][0], self.__board[6][1], self.__board[6][2],
                       self.__board[7][0], self.__board[7][1], self.__board[7][2],
                       self.__board[8][0], self.__board[8][1], self.__board[8][2]]
        elif ((6 <= row_of_num <= 8) and (3 <= col_of_num <= 5)):  # If in box 7
            cur_box = [self.__board[6][3], self.__board[6][4], self.__board[6][5],
                       self.__board[7][3], self.__board[7][4], self.__board[7][5],
                       self.__board[8][3], self.__board[8][4], self.__board[8][5]]
        else:  # If in box 8
            cur_box = [self.__board[6][6], self.__board[6][7], self.__board[6][8],
                       self.__board[7][6], self.__board[7][7], self.__board[7][8],
                       self.__board[8][6], self.__board[8][7], self.__board[8][8]]
        # Check if num is found in cur_box once
        if cur_box.count(num) == 1:  # Check if num is found in cur_col once
            return True
        else:
            return False

    # Checks if cur num is valid
    def __is_valid(self, row_of_num, col_of_num):
        num = self.__board[row_of_num][col_of_num] 
        if self.__valid_in_row(num, row_of_num) and self.__valid_in_col(num, col_of_num) and self.__valid_in_box(num, row_of_num, col_of_num):
            return True
        else:
            return False
        
    def solve(self):
        for ()