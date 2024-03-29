class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")" : "(",
                  "}" : "{",
                  "]" : "["}
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) and mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        