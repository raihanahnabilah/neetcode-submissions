class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # time complexity: O(n)
        # space complexity: O(n)

        # 1. clean the string
        splitS = list(s)
        cleanedS = [char_s.lower() for char_s in splitS if char_s.isalnum()]
        reversedCleanedS = reversed(cleanedS)

        # 2. reverse the string
        return cleanedS == list(reversedCleanedS)