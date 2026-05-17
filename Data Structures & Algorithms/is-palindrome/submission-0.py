class Solution:
    def isPalindrome(self, s: str) -> bool:
        # This is two pointers
        # One at the beginning, the other at the end
        cleanedString = ''.join(char.lower() for char in s if char.isalnum())

        leftPointer = 0
        rightPointer = len(cleanedString) - 1

        while leftPointer <= rightPointer:
            if cleanedString[leftPointer] != cleanedString[rightPointer]:
                return False
            leftPointer += 1
            rightPointer -= 1
        
        return True



        