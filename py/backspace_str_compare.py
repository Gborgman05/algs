class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack2 = []
        for char in s:
            if char == "#" and stack:
                stack.pop()
            elif char != "#":
                stack.append(char)
        for char in t:
            if char == "#" and stack2:
                stack2.pop()
            elif char != "#":
                stack2.append(char)
        return stack == stack2