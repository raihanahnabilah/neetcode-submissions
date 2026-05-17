class Solution:
    def isValid(self, s: str) -> bool:
    
        # time complexity: O(n)
        # space complexity: O(n/2)

        open_stack = [] 
        open_to_closed = {"(": ")", "{": "}", "[": "]"}

        if len(s) <= 1:
            return False

        for char in s:
            if char == "(" or char == "[" or char == "{":
                open_stack.append(char)
            else:
                if open_stack:
                    popped = open_stack.pop()
                    if char != open_to_closed[popped]:
                        return False
                else:
                    return False

        if open_stack:
            return False 
        
        return True

