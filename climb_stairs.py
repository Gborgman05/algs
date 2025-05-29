class Solution:
    def climbStairs(self, n: int) -> int:
        items = [1, 2]
        while len(items) < n:
            items.append(items[-1] + items[-2])
        return items[n -1]