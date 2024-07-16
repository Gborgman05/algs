class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(matrix)
        if len(matrix) <= 0:
            return False
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target
        l = 0
        r2 = len(matrix)
        l2 = 0
        r = len(matrix[0])
        pivot = (l + r) // 2
        pivot2 = (l2 + r2) // 2
        print(pivot)
        print(pivot2)
        if matrix[pivot2][pivot] == target:
            return True
        elif matrix[pivot2][pivot] < target:
            print(matrix[pivot2:][:pivot])
            return (self.searchMatrix(matrix[pivot2:][:pivot], target) or # upper right
                    self.searchMatrix(matrix[pivot2:][pivot:], target) or # lower right
                   self.searchMatrix(matrix[:pivot2][pivot:], target)) #lower left
        elif matrix[pivot2][pivot] > target:
            return (self.searchMatrix(matrix[pivot2:][:pivot], target) or # upper right
                    self.searchMatrix(matrix[:pivot2][:pivot], target) or # upper left
                   self.searchMatrix(matrix[:pivot2][pivot:], target)) #lower left
        return False
        # while l <= r:

        #     if matrix[pivot2][pivot] > target:
        #         pass
        #     elif matrix[pivot2][pivot] < target:
                