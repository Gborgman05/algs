class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(x, y, board):
            #check to the left
            l = x - 1
            while l >= 0:
                if board[l][y] == "Q":
                    return False
                l -= 1
            # check back diagonal
            l = x - 1
            u = y - 1
            while l >= 0 and u >= 0:
                if board[l][u] == "Q":
                    return False
                l -= 1
                u -= 1
            
            #check other back diagonal:
            l = x - 1
            u = y + 1
            while u < len(board) and l >= 0:
                if board[l][u] == "Q":
                    return False
                l -= 1
                u += 1
            return True
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if isSafe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."

        backtrack(0)
        return res


        