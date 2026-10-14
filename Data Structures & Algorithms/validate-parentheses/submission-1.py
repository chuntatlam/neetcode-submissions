class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif not stack or s[i] == ")":
                if stack.pop() != "(":
                    return False
            elif not stack or s[i] == "}":
                if stack.pop() != "{":
                    return False
            elif not stack or s[i] == "]":
                if stack.pop() != "[":
                    return False
        return not stack
        