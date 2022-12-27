class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = [1 for i in range(len(matrix))]
        xs = [1 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] is None or matrix[i][j]:
                    if zeros[i] == 0 or xs[j] == 0:
                        matrix[i][j] = None
                else:
                    zeros[i] = 0
                    xs[j] = 0
                    for k in range(len(matrix[i])):
                        if matrix[i][k]:
                            matrix[i][k] = None 
                    for k in range(len(matrix)):
                        if matrix[k][j]:
                            matrix[k][j] = None 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
                        