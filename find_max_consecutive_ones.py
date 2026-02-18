class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        is_one = False
        max_len = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                if is_one:
                    count += 1
                else:
                    count = 1
                is_one = True
            else:
                count = 0
                is_one = False
            max_len = max(max_len, count)
        return max_len
            
        