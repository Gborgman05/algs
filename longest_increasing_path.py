class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_length = 0
        paths = [[0] * len(matrix[0]) for _ in matrix]

        def dfs(i, j, val):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= val:
                return 0
            # print(i)
            # print(j)
            # print(val)
            if paths[i][j] > 0:
                return paths[i][j]
            max_path = 0
            max_path = max(dfs(i-1, j, matrix[i][j]), max_path)
            max_path = max(dfs(i, j-1, matrix[i][j]), max_path)
            max_path = max(dfs(i, j+1, matrix[i][j]), max_path)
            max_path = max(dfs(i+1, j, matrix[i][j]), max_path)
            paths[i][j] = max_path + 1
            return max_path + 1


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                length = dfs(i, j, -float("inf"))
                max_length = max(length, max_length)
        return max_length

        