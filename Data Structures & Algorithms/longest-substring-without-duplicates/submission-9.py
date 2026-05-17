class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxRes = 0

        # some sort of looping! not sure yet
        # need to do for loop still!
        for i, char in enumerate(s):
            isSeen = set()
            start = i
            end = i + 1

            isSeen.add(char)
            maxRes = max(maxRes, 1)

            while end < len(s) and s[end] not in isSeen:
                isSeen.add(s[end])
                maxRes = max(maxRes, (end-start) + 1)
                end += 1

        return maxRes        





            
