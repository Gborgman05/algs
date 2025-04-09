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
        