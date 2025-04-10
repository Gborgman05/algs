class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if stack and stack.pop() == mapping[char]:
                    continue
                else:

                    return False
        return not stack 