class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [("", 0)]
        final = []
        while stack:
            curr, l = stack.pop()
            if len(curr) >= 2*n :
                if l == 0:
                    final.append(curr)
            else:
                stack.append((curr + "(", l + 1))
                if l > 0:
                    stack.append((curr + ")", l - 1))
        return final