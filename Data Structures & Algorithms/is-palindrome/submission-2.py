class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string first
        cleanedString = [char.lower() for char in s if char.isalnum()]
        cleanedStringBack = "".join(cleanedString);

        # Then reverse and compare the values
        return cleanedStringBack == "".join(reversed(cleanedStringBack))
