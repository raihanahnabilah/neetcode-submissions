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
        maxLength = 0
        maxString = ""
        uniqueChars = set()
        for char in s:
            if char in uniqueChars:
                index = 0
                print("Checking maxString", maxString)
                while maxString[index] != char and index < len(maxString):
                    uniqueChars.remove(maxString[index])
                    index += 1
                maxString = maxString[index + 1:] + char
            else:
                uniqueChars.add(char)
                maxString += char
            maxLength = max(maxLength, len(maxString))

        return maxLength

