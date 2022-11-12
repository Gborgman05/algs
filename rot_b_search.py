class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        def find_rot(nums):
            strt = 0 
            nd = len(nums)-1
            while strt < nd:
                mid = (strt + nd) // 2
                if nums[nd] < nums[mid]:
                    strt = mid + 1
                else:
                    nd = mid
            return strt
        # while True:
        rot = find_rot(nums)
        # print("rot is", rot)
        while start <= end:
            mid = (start + end) // 2
            # print(mid)
            if nums[(mid + rot) % len(nums)] < target:
                start = mid + 1
            elif nums[(mid + rot) % len(nums)] > target:
                end = mid - 1
            else:
                return (mid + rot) %len(nums)
        return -1
            
                
                
            
            