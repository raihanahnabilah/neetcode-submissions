class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Solution 1: Would be brute force
        def validPalindrome(strPalindrome: str):

            # This is if length is odd
            if len(strPalindrome) % 2 != 0:
                middle = len(strPalindrome) // 2
                left = right = middle
                while left >= 0 and right < len(strPalindrome):
                    if strPalindrome[left] != strPalindrome[right]:
                        return False
                    left -= 1
                    right += 1
                
                # print("Checking left and right", left, right, strPalindrome)
                if left >= 0 or right < len(strPalindrome):
                    return False
                
                return True
            
            else:
                left = 0
                right = len(strPalindrome) - 1
                while left <= right:
                    if strPalindrome[left] != strPalindrome[right]:
                        return False
                    left += 1
                    right -= 1
                return True
        
        longestSubstring = ""
        maxLength = 0

        for i in range(len(s)):
            for j in range(len(s[i:])):
                currentString = s[i:i+j+1]
                isPalindrome = validPalindrome(currentString)
                # print("Checking the i j", i, j, s[i+1:])
                # print("Checking currentString and isPalindrome", currentString, isPalindrome, (i+j+1)-i, maxLength)
                if ((i+j+1) - i) > maxLength and isPalindrome:
                    longestSubstring = currentString
                    maxLength = (i+j+1) - i
                
        return longestSubstring
