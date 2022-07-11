# https://leetcode.com/problems/binary-search/submissions/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
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