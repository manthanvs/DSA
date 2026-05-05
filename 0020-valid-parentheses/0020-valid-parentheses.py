class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpenDict = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:
            if char in closeToOpenDict:
                if stack and stack[-1] == closeToOpenDict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False