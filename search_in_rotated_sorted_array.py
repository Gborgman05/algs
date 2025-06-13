class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            if nums[l] < nums[mid]:
                # rotation is between mid and right, or at the end
                if target > nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # rotation is between mid and left
                if target > nums[mid] and target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
