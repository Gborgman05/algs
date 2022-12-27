class Solution:
    def permute(self, num: List[int]) -> List[List[int]]:
        n = len(num)
        ans = []

        def solve(nums, j):
            if j == n:
                ans.append(nums[:])

            for i in range(j, n):
                nums[i], nums[j] = nums[j], nums[i]
                solve(nums, j+1)
                nums[i], nums[j] = nums[j], nums[i]

        solve(num, 0)
        return ans