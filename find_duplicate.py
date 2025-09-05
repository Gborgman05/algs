class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # first go until you've seen the same thing twice
        # then do cycle detection
        fast = nums[0]
        slow = nums[0]

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        
        second = nums[0]
        while second != slow:
            second = nums[second]
            slow = nums[slow]
        return slow
