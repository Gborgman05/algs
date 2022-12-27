class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        srted = sorted(heights)
        cnter = 0
        for i, j in zip(srted, heights):
            if i != j:
                cnter += 1
        return cnter