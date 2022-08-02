class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        final = []
        while len(matrix) > 0: 
            if matrix:
                final.extend(matrix.pop(0))
            if matrix and matrix[0]:
                final.extend([row.pop(-1) for row in matrix])
            if matrix:
                final.extend(reversed(matrix.pop(-1)))
            if matrix and matrix[0]:
                final.extend(reversed([row.pop(0) for row in matrix]))
        return final
     
        