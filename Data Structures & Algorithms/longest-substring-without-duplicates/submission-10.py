class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Time complexity: O(n*m) -> this is brute force
        # where n is the length of the string and 
        # m is the total number of unique characters in the string
        # maxRes = 0

        # for i, char in enumerate(s): 
        #     isSeen = set()
        #     start = i
        #     end = i + 1

        #     isSeen.add(char)
        #     maxRes = max(maxRes, 1)

        #     while end < len(s) and s[end] not in isSeen: 
        #         isSeen.add(s[end])
        #         maxRes = max(maxRes, (end-start) + 1)
        #         end += 1

        # return maxRes        

        # Sliding window
        maxRes = 0
        isSeen = set()
        leftPointer = 0
        for rightPointer, num in enumerate(s):
            if num in isSeen:
               while num in isSeen:
                    isSeen.remove(s[leftPointer])
                    leftPointer += 1
            isSeen.add(num)
            maxRes = max(maxRes, rightPointer - leftPointer + 1)

        return maxRes    





            
