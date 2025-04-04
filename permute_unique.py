class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = {}
        for a in nums:
            if a in counts:
                counts[a] += 1
            else:
                counts[a] = 1
        sol = []
        def helper(curr, counts):
            if len(curr) == len(nums):
                sol.append(list(curr))
                return []
            else:
                for key in counts:
                    if counts[key] > 0:
                        counts[key] -= 1
                        curr.append(key)
                        helper(curr, counts)
                        curr.pop()
                        counts[key] += 1
        helper([], counts)
        return sol
        