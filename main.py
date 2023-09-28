import board
board1 = board.Board([[None, 7, None, None, 1, 4, None, None, None],
                      [6, 1, 2, None, 9, 5, 3, 8, None],
                      [3, None, 4, None, 6 ,8, 9, 7, 1],
                      [None, None, None, 1, None, None, None, 5, None],
                      [2, 8, None, None, None, None, 7, None, 3],
                      [5, None, 3, None, 8, None, None, None, None],
                      [None, 2, None, None, 3, None, None, None, None],
                      [None, None, 6, 8, None, None, 1, None, 5],
                      [None, None, None, 6, 7, None, 4, 3, None]])
board2 = board.Board([[None, 7, 5, None, 9, None, None, None, 6],
                      [None, 2, 3, None, 8, None, None, 4, None],
                      [8, None, None, None, None, 3, None, None, 1],
                      [5, None, None, 7, None, 2, None, None, None],
                      [None, 4, None, 8, None, 6, None, 2, None],
                      [None, None, None, 9, None, 1, None, None, 3],
                      [9, None, None, 4, None, None, None, None, 7],
                      [None, 6, None, None, 7, None, 5, 8, None],
                      [7, None, None, None, 1, None, 3, 9, None]])
board1.print()