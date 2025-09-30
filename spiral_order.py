class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, t = 0, 0
        r, b = len(matrix[0]), len(matrix)
        final = []
        while l < r and t < b:
            for i in range(l, r):
                final.append(matrix[t][i])
            t += 1
            for i in range(t, b):
                final.append(matrix[i][r-1])
            r -= 1
            if not (l < r and t < b):
                break
            for i in range(r-1, l-1, -1):
                final.append(matrix[b-1][i])
            b -= 1
            for i in range(b-1, t-1, -1):
                final.append(matrix[i][l])
            l +=1
        return final