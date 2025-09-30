class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    #matrix[i][j] = None
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None
                    for l in range(len(matrix[0])):
                        if matrix[i][l] != 0:
                            matrix[i][l] = None
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        