class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time complexity: O(nlogn)
        # space complexity: O(1)
        return sorted(s) == sorted(t)
