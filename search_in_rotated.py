class Solution:
    def search(self, nums: List[int], target: int) -> int:
        highest = nums[0]
        # first determine where the greatest or smallest value is in the array:
        low = 0
        high = len(nums) -1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid+1
        rot = low
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[(mid + rot) % len(nums)] == target:
                return (mid + rot) % len(nums)
            elif nums[(mid + rot) % len(nums)] < target:
                low = mid + 1
            elif nums[(mid + rot) % len(nums)] > target:
                high = mid - 1
        return -1
