class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # # time complexity: O(n)
        # # space complexity: O(n)

        # # 1. clean the string
        # splitS = list(s)
        # cleanedS = [char_s.lower() for char_s in splitS if char_s.isalnum()]
        # reversedCleanedS = reversed(cleanedS)

        # # 2. reverse the string
        # return cleanedS == list(reversedCleanedS)

        ## Solution 2 for O(1) space complexity:
        # space complexity: O(1)
        # time complexity: O(n)
        # two pointers
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer <= right_pointer:
            # For cleaning up
            if not s[left_pointer].isalnum():
                left_pointer += 1
                continue
            if not s[right_pointer].isalnum():
                right_pointer -= 1
                continue

            # For checking
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            else:
                left_pointer += 1
                right_pointer -= 1
        
        return True



