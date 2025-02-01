class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        last = None
        for num in nums:
            curr = num % 2
            if last is not None:
                if curr == last:
                    return False
            last = curr
        return True 
        