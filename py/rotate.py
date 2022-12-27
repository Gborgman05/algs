class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
#         m_size = len(matrix)
#         def one_rot(indices):
#             cur_x, cur_y = indices
#             indices = [indices, 
#                        (cur_x, m_size -cur_y - 1), 
#                        (m_size - cur_x - 1, m_size - cur_y - 1), 
#                        (m_size - cur_x - 1, cur_y)]
#             # print(indices)
#             vals = [matrix[index[0]][index[1]] for index in indices]
#             for i in range(1, len(vals)):
#                 matrix[indices[i][0]][indices[i][1]] = vals[i-1]
#             matrix[indices[0][0]][indices[0][1]] = vals[-1]
#         one_rot((0, 0))
#         # for all elements in top left corner rotate them
#         def ceil(a, b):
#             # reverse floor division
#             return -(a // -b)
#         to_rotate = ceil(m_size, 2)
#         cand = []
#         for x in range(m_size // 2 + m_size % 2):
#             for y in range(m_size // 2):
#                 print(x, y)
#                 one_rot((x, y))
#         return matrix
        
#         # print(matrix)
                
