class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        def eval_op(operands, operator):
            if operator == "+":
                return int(operands[0]) + int(operands[1])
            elif operator == "-":
                return int(operands[0]) - int(operands[1])
            elif operator == "*":
                return int(operands[0]) * int(operands[1])
            elif operator == "/":
                return int(operands[0]) / int(operands[1])
        stack = []
        for token in tokens:
            if token in ops:
                a = stack.pop()
                b = stack.pop()
                operands = [b, a]
                stack.append(eval_op(operands, token))
            else:
                stack.append(token)
        return int(stack[0])