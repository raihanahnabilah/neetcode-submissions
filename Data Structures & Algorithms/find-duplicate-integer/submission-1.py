class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniqueNums = set()

        for num in nums:
            if num in uniqueNums:
                return num
            else:
                uniqueNums.add(num)
        