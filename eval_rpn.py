class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                # print(stack)
                r = stack.pop()
                l = stack.pop()
                res = 0
                if token == "+":
                    res = l + r
                elif token == "-":
                    res = l - r
                elif token == "*":
                    res = l * r
                elif token == "/":
                    # print(l)
                    # print(r)
                    res = l / r
                    if res < 0:
                        res = math.ceil(res)
                    else:
                        res = math.floor(res)
                    # print(res)
                else:
                    assert False
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]


        