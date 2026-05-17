class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(1) space is a bit complicated... I can do with O(n) space for now
        unique_num = set()
        for num in nums:
            if num in unique_num:
                return num
            else:
                unique_num.add(num)
        