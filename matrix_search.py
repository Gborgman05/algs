import pdb
class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        # idea is binary search one way, then the other way
        def binary_search(arr):
            low = 0
            high = len(arr) - 1
            mid = (high + low) // 2
            pdb.set_trace()
            print(arr)
            print(high)
            print(mid)
            while low < high:
                mid = low + (high - low) // 2
                # 2 + 5 // 2
                # 0 1 2 3 4 5 
                if target == arr[mid]:
                    return mid
                elif target < arr[mid]:
                    high = mid - 1
                elif target > arr[mid]:
                    low = mid + 1
                else:
                    print("fail")
            return low
        print("here")
        # pdb.set_trace()
        pos_y = binary_search([sub[0] for sub in matrix])
        print("passes")
        pos_x = binary_search(matrix[pos_y])
        print(matrix[pos_y][pos_x])
        return matrix[pos_y][pos_x] == target

Solution().searchMatrix([[1, 1]], 0)class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # idea is binary search one way, then the other way
        def binary_search(arr):
            low = 0
            high = len(arr) - 1
            mid = (high + low) // 2
            # pdb.set_trace()
            print(arr)
            print(high)
            print(mid)
            while low < high:
                mid = low + (high - low) // 2
                # 2 + 5 // 2
                # 0 1 2 3 4 5 
                if target == arr[mid]:
                    return mid
                elif target < arr[mid]:
                    high = mid - 1
                elif target > arr[mid]:
                    low = mid + 1
                else:
                    print("fail")
            return low
        print("here")
        # pdb.set_trace()
        pos_y = binary_search([sub[0] for sub in matrix])
        if matrix[pos_y][0] > target:
            pos_y -= 1
        # print("passes")
        pos_x = binary_search(matrix[pos_y])
        print(matrix[pos_y][pos_x])
        return matrix[pos_y][pos_x] == target
                    
                
        