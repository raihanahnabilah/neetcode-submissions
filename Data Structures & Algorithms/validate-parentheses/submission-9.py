class Solution:
    def isValid(self, s: str) -> bool:
        # (), [], {}

        # (()[]) - True -> counter of open and closing brackets
        # ((){) - False

        # (()[])
        # open_bracket = 3
        # closing_bracket = 3
        # (())
        # so need to match the brackets
        
        # keep a stack of open_brackets: and the match
        if len(s) <= 1:
            return False

        openBrackets = []
        openBracketToClosedBracket = {"(": ")", "[": "]", "{": "}"}
        for bracket in s:
            if bracket == "[" or bracket == "{" or bracket == "(":
                openBrackets.append(bracket)
            else:
                if openBrackets:
                    openBracket = openBrackets.pop()
                    if bracket != openBracketToClosedBracket[openBracket]:
                        return False
                else:
                    return False
        
        if openBrackets:
            return False
            
        return True
            





        

