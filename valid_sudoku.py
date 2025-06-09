class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(len(board))] 
        columns = [{} for _ in range(len(board))] 
        squares = [{} for _ in range(len(board))] 
        #print(squares)
        for i in range(len(board)):
            for j in range(len(board[0])):
                entry = board[i][j]
                if entry == ".":
                    continue
                    # 
                #print(squares[(3*(i//3) + (j // 3))])
                if entry in rows[i] or entry in columns[j] or entry in squares[(3*(i//3) + (j // 3))]:
                    # print(i, j)
                    # print(rows[i])
                    # print(entry)
                    # print(rows)
                    return False
                rows[i][entry] = 1
                columns[j][entry] = 1
                squares[(3*(i//3) + (j // 3))][entry] = 1
        return True