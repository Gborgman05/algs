class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = {}
        for a in nums:
            if a in counts:
                counts[a] += 1
            else:
                counts[a] = 1
        sol = []
        for char in counts:
            sol.append(char)
            if counts[char] <= 1:
                del counts[char]
            else:
                counts[char] -= 1
    def helper(self, curr):
        next_level = []
        for i in range(len(curr)):
            poss = curr[0]
            for char in poss:
                new_poss = char
                next_level.append([curr[i][1] + [char])
        return next_level
