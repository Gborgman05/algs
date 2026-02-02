class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        back_to_front = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        for char in s:
            if char in back_to_front:
                if stack and stack[-1] == back_to_front[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
        