class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        stack = []
        j = 1
        ops = []
        while len(target) != len(stack):
            stack.append(j)
            ops.append("Push")
            if stack[-1] != target[i]:
                stack.pop()
                ops.append("Pop")
            else:
                i += 1
            j += 1
        return ops

