class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_set = {"+", "-", "*", "/"}
        for token in tokens:
            if token == "+":
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif token == "-":
                result = stack.pop() - stack.pop()
                stack.append(result)
            elif token == "*":
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif token == "/":
                result = stack.pop() / stack.pop()
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]
            
