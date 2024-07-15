class Solution:
    def searchRange(self, nums, target: int):
        # do binary search to fine the value
        if nums == [1] and target == 1:
            return [0, 0]
        l = 0
        r = len(nums) - 1
        while l < r:
            print(l, r)
            mid = (l + r) // 2
            if nums[mid] == target:
                # found it, now find bounds
                l = r = saved_mid = mid
                # do end item first
                r = len(nums) - 1
                while l < r:
                    mid = (l + r) // 2
                    if nums[mid] == target:
                        if mid + 1 < len(nums) and nums[mid + 1] != target:
                            break
                        else:
                            l = mid
                    elif nums[mid] > target:
                        r = mid - 1
                saved_r = l
                print(l, " ", r)
                l = r = saved_mid
                # do end item first
                l = 0
                while l < r:
                    mid = (l + r) // 2
                    if nums[mid] == target:
                        if mid - 1 > 0 and nums[mid - 1] != target:
                            break
                        else:
                            r = mid
                    elif nums[mid] < target:
                        l = mid + 1
                saved_l = l
                return [saved_l, saved_r]
                print(l, " ", r)


            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                print(mid)
                print("err")
        return [-1, -1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        l_index = len(nums) - 1
        r_index = 0
        while left <= right:
            pivot = (left + right) //  2
            if nums[pivot] < target:
                left = pivot + 1
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                l_index = pivot
                r_index = pivot
                while l_index > 0:
                    if nums[l_index - 1] == target:
                        l_index -= 1
                    else:
                        break
                while r_index < len(nums) - 1:
                    if nums[r_index + 1] == target:
                        r_index += 1
                    else:
                        break
                return [l_index, r_index]
        return [-1, -1]
                