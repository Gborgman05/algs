class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = cur_min = 1

        for n in nums:
            temp = cur_max * n
            cur_max = max(temp, cur_min * n, n)
            cur_min = min(temp, cur_min * n, n)

            res = max(res, cur_max)
        
        return res

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        fin = 0
        total = nums[0]
        fin = total

        for num in nums[1:]:
            if total < 0:
                total = 0
            total += num
            fin = max(fin, total)
        return fin

        