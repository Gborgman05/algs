class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = 1
        res = nums[0]

        for num in nums:
            temp = curr_max * num
            curr_max = max(num, temp, num * curr_min) 
            curr_min = min(num, temp, num * curr_min)

            res = max(res, curr_max)
        return res


        