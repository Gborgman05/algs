class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j, found=False):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if (found or (i == 0 or j == 0 or i == m - 1 or j == n - 1)) and (board[i][j] == 'O' or board[i][j] == 'Z'):
                board[i][j] = 'Y'
                for d in direct:
                    dfs(i + d[0], j + d[1], True)
                return True
            elif board[i][j] == 'O':
                board[i][j] = 'Z'
                for d in direct:
                    dfs(i + d[0], j + d[1])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    dfs(i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "Z":
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'


                    # check connected and find if any are on the edges
