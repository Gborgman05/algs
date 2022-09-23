class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= len(nums):
                nums[i] = 0
        for i in range(len(nums)):
            nums[nums[i] % n] += n
        print(nums)
        for i in range(n):
            if nums[i] // n <= 0:
                print(nums[i])
                print(i + 1)
                return i
        return n
        # mn = 0
        # for num in nums:
        #     if mn == 0 and num > 0:
        #         mn = num
        #     if num < mn and num > 0:
        #         mn = num
        # if mn > 1:
        #     return 1
        # ptr = mn
        # for num in nums:
        #     if num == ptr + 1:
        #         ptr += 1
        # return ptr + 1
        