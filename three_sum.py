class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fix the middle point
        final = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                #print([nums[l], nums[i], nums[r]])
                tmp = nums[l] + nums[i] + nums[r]
                if tmp == 0:
                    final.append([nums[l], nums[i], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                elif tmp > 0:
                    r -= 1
                elif tmp < 0:
                    l += 1
        return final


        