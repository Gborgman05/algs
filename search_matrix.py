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
                
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do binary search on first number in each row, then on the row
        top = 0
        bottom = len(matrix) - 1
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target
        while top <= bottom:
            midpoint = (bottom + top) // 2
            if matrix[midpoint][0] > target:
                bottom = midpoint - 1
            elif matrix[midpoint][0] < target:
                top = midpoint + 1
            else:
                return True
        l = 0
        r = len(matrix[0]) - 1
        row = bottom
        while l <= r:
            midpoint = (l + l) // 2
            if matrix[row][midpoint] > target:
                r = midpoint - 1
            elif matrix[row][midpoint] < target:
                l = midpoint + 1
            else:
                return True
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search first column
        top = 0
        bottom = len(matrix) -1
        while top <= bottom:
            mid = (top + bottom) // 2
            print(mid)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
        l = 0 
        r = len(matrix[0]) - 1
        print(bottom)
        if bottom >= len(matrix) or bottom < 0:
            return False

        while l <= r:
            mid = (l + r) // 2
            if matrix[bottom][mid] == target:
                return True
            elif matrix[bottom][mid] < target:
                l = mid + 1
            elif matrix[bottom][mid] > target:
                r = mid - 1
        return False