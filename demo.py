
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    board_length = len(board)

    square = {
        0: 0,
        1: 0,
        2: 0,
        3: 3,
        4: 3,
        5: 3,
        6: 6,
        7: 6,
        8: 6
    }

    for i in range(board_length):
        for j in range(board_length):
            ele = board[i][j]
            if ele == ".":
                continue

            # Checking row and column
            for k in range(board_length):
                if [i, j] == [4, 4]:
                    print(board[i][k])
                if [i, j] == [i, k] or [i, j] == [k, j]:
                    continue
                elif board[i][k] == ele or board[k][j] == ele:
                    return False

            # Selecting square box
            for key in square.keys():
                if i == key:
                    start_row = square[key]
                if j == key:
                    start_column = square[key]

            # Checking Square Box:
            for m in range(start_row, start_row + 3):
                for n in range(start_column, start_column + 3):
                    if [i, j] == [m, n]:
                        continue
                    if ele == board[m][n]:
                        return False

    return True


l = [["7",".",".",".","4",".",".",".","."],[".",".",".","8","6","5",".",".","."],[".","1",".","2",".",".",".",".","."],[".",".",".",".",".","9",".",".","."],[".",".",".",".","5",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".","2",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

print(isValidSudoku((l)))