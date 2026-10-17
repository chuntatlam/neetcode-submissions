class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "+":
                a, b = stack[-1], stack[-2]
                stack.append(int(a) + int(b))
            elif o == "D":
                stack.append(int(stack[-1]) * 2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))
            print(stack)
        return sum(stack)