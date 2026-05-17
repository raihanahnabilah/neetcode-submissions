class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesMap = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        stack = []

        for char in s:
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
            else:
                if len(stack) > 0:
                    matched = stack.pop()
                    if matched != parenthesesMap[char]:
                        return False
                else:
                    return False
                    
        if len(stack) > 0:
            return False

        return True


