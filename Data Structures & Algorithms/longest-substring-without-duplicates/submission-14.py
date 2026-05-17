class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # zxyzxyz
        # keep track of seen characters
        # z is not seen - count: 1, compare against maxCount
        # x is not seen - count: 2, compare against maxCount
        # y is not seen - count: 3, compare against maxCount
        # z is seen - move left pointer to until there it's not in seen anymore, then count

        # time complexity: O(n)
        # space complexity: O(1)
        if len(s) <= 1:
            return len(s)

        left_pointer = 0
        right_pointer = 1

        isSeen = set()
        isSeen.add(s[left_pointer])

        res = 0

        while left_pointer <= right_pointer and right_pointer < len(s):
            if s[right_pointer] in isSeen:
                while s[left_pointer] != s[right_pointer]:
                    isSeen.remove(s[left_pointer])
                    left_pointer += 1
                left_pointer += 1
            else:
                isSeen.add(s[right_pointer])
            res = max(res, right_pointer - left_pointer + 1)
            right_pointer += 1

        return res
