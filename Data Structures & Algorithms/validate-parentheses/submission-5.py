class Solution:
    def isValid(self, s: str) -> bool:
        # ([]{}) - stack
        # if the open bracket -> ([
        # if closing bracket -> pop from open bracket = check if they are of the same type -> y

        if len(s) % 2 != 0:
            return False

        open_brackets = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                open_brackets.append(char)
            else:
                if len(open_brackets) == 0:
                    return False

                open_bracket = open_brackets.pop()
                if char == ")":
                    expected_open_bracket = "("
                elif char == "]":
                    expected_open_bracket = "["
                elif char == "}":
                    expected_open_bracket = "{"
                
                if open_bracket != expected_open_bracket:
                    return False

        if len(open_brackets) > 0:
            return False

        return True





            
        
