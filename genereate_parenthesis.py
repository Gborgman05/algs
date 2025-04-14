class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        def helper(so_far, left, right, total):
            if left == right and right == total:
                final.append(so_far)
                return so_far
            else:
                if left < total and right < left:
                    helper(so_far + "(", left+1, right, total)
                    helper(so_far + ")", left, right+1, total)
                elif left < total:
                    helper(so_far + "(", left+1, right, total)
                elif right < left:
                    helper(so_far + ")", left, right+1, total)
        helper("", 0, 0, n)
        return final

