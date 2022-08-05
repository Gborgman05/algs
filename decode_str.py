class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        final = ""
        i = 0
        while i < len(s):
            # print(s[i])
            if s[i] == "]":
                chars = stack.pop()
                bracket = stack.pop()
                print(chars)
                print(bracket)
                num = int(stack.pop())
                print(stack)
                if stack and ord(stack[-1][0]) >= ord("a") and ord(stack[-1][0]) <= ord("z"):
                    stack[-1] = stack[-1] + chars*num
                else:
                    stack.append(chars*num)
                i += 1
            elif s[i] == "[":
                stack.append(s[i])
                i += 1
            elif ord(s[i]) <= ord("9") and ord(s[i]) >= ord("0"):
                num = ""
                while ord(s[i]) <= ord("9") and ord(s[i]) >= ord("0"):
                    num += s[i]
                    i += 1
                stack.append(num)
            elif ord(s[i]) >= ord("a") and ord(s[i]) <= ord("z"):
                num = ""
                while i < len(s) and ord(s[i]) >= ord("a") and ord(s[i]) <= ord("z"):
                    num += s[i]
                    i += 1
                stack.append(num)
            else:
                print("fail")
        return "".join(stack)
            