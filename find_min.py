class Solution:
    # this solution struggled for the case where it was not rotated
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r and l != r-1:
            midpoint = (l + r) // 2
            if nums[midpoint] > nums[l]:
                # rotation is between mid and r
                l = midpoint
            elif nums[midpoint] < nums[l]:
                r = midpoint
            else:
                assert False
        print(l, " ", r)
        if nums[0] < nums[r]:
            return nums[0]
        return nums[r]
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
