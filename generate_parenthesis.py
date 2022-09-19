# memory optimized
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(s, l, r):
            # print(s)
            if l == r == 0:
                # print(s)
                return [s]
            if l > 0 and r > l:
                return helper(s + "(", l-1, r) + helper(s + ")", l, r-1)
            elif l >0 and l == r:
                return helper(s + "(", l-1, r)
            else:
                return helper(s + ")", l, r-1)
        return helper("", n, n)
        