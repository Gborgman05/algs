class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9) ]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        def calc_box(i, j):
            return i // 3 + (j // 3) * 3
        for i in range(len(board)):
            for j in range(len(board[0])):
                tmp = board[i][j]
                if tmp == '.':
                    continue
                if tmp in rows[i] or tmp in columns[j] or tmp in boxes[calc_box(i, j)]:
                    return False
                else:
                    rows[i][tmp] = 1
                    columns[j][tmp] = 1
                    boxes[calc_box(i, j)][tmp] = 1
        return True
        


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in board]
        columns = [{} for _ in board]
        squares = [{} for _ in board]
        def get_square(row, col):
            return 3 *(row // 3) + col // 3
        for row in range(len(board)):
            for col in range(len(board)):
                char = board[row][col]
                if char not in (".", ",") and (char in rows[row] or char in columns[col] or char in squares[get_square(row, col)]):
                    print(row, " ", col, " ", char)
                    return False
                rows[row][char] = 1
                columns[col][char] = 1
                squares[get_square(row, col)][char] = 1
        return True