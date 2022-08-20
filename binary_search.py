import pdb
# https://leetcode.com/problems/binary-search/submissions/
class Solution:
    def search(self, nums) -> int:
        def sub_search(nums, target, min_index, max_index):
            index = (max_index + min_index) // 2
            if max_index < min_index:
                return -1
            elif nums[index] == target:
                return index
            elif nums[index] > target:
                return sub_search(nums, target, min_index, index - 1)
            else:
                return sub_search(nums, target, index + 1, max_index)
        max_index = len(nums) - 1
        min_index = 0
        return sub_search(nums, target, min_index, max_index)
 
def bin_search(nums, target):
    a = 0
    z = len(nums) - 1
    # pdb.set_trace()
    while a <= z:
        mid = (z - a) // 2 + a
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            z = mid - 1
        else:
            a = mid + 1
    return -1
        