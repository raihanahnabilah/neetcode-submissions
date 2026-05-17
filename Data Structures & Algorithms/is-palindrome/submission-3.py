class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string first
        # Time complexity: O(n)
        # Space complexity: O(n)
        cleanedString = "".join(char.lower() for char in s if char.isalnum());

        # Then reverse and compare the values
        return cleanedString == "".join(reversed(cleanedString))
