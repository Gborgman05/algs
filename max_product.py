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


        
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min = cur_max = 1

        for num in nums:
            tmp = cur_max * num
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(tmp, num * cur_min, num)
            res = max(res, cur_max)
        return res