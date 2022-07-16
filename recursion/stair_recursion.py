# https://leetcode.com/explore/featured/card/recursion-i/255/recursion-memoization/1662/
class Solution:
    def climbStairs(self, n: int) -> int:
        store = {}
        def helper(n):
            if n < 2:
                return 1
            elif n in store:
                return store[n]
            else:
                new = helper(n-1) + helper(n-2)
                store[n] = new
                return new
        return helper(n)
        