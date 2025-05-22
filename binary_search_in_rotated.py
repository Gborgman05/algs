class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (r + l) // 2
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            if target == nums[mid]:
                return mid

            if nums[l] < nums[mid]:
                # switch is between mid and r
                if target > nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # switch is between l and mid
                if target > nums[mid] and target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return r if nums[r] == target else -1
