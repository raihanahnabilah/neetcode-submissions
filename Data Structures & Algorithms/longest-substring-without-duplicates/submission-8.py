class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # z
        # zx
        # zxy
        # zxyz -> is already there, so remove it and add again
        # xyz
        # xyzx -> is already there so remove it and add again
        # yzx
        #

        #abcbac
        # a
        # ab
        # abc
        # abcb

        # Method 1: Brute force
        # maxLength = 0
        # maxString = ""
        # uniqueChars = set()
        # for char in s:
        #     if char in uniqueChars:
        #         index = 0
        #         while maxString[index] != char and index < len(maxString):
        #             uniqueChars.remove(maxString[index])
        #             index += 1
        #         maxString = maxString[index + 1:] + char
        #     else:
        #         uniqueChars.add(char)
        #         maxString += char
        #     maxLength = max(maxLength, len(maxString))

        # return maxLength

        # Method 2: Sliding window
        uniqueChars = set()
        maxLength = 0
        l = 0

        for r in range(len(s)):
            while s[r] in uniqueChars:
                uniqueChars.remove(s[l])
                l += 1
            uniqueChars.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength

