class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        seen = {}
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp > 0:
                    k -= 1
                elif tmp < 0:
                    j += 1
                else:
                    add = [nums[i], nums[j], nums[k]]
                    check = str(add)
                    if check not in seen:
                        triplets.append([nums[i], nums[j], nums[k]])
                        seen[check] = 1
                    j += 1
                    k -= 1
        return triplets