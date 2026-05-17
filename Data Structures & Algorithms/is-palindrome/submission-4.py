class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # First solution
        # # Clean the string first
        # # Time complexity: O(n)
        # # Space complexity: O(n)
        # cleanedString = "".join(char.lower() for char in s if char.isalnum());

        # # Then reverse and compare the values
        # return cleanedString == "".join(reversed(cleanedString))

        # Second solution:
        # Two pointers
        left = 0
        right = len(s) - 1
        while left <= right:
            charLeft = s[left]
            charRight = s[right]

            if charLeft.isalnum() == False:
                left += 1
                continue
            if charRight.isalnum() == False:
                right -= 1
                continue
            if charLeft.lower() != charRight.lower():
                return False
            else:
                left += 1
                right -= 1
        return True




