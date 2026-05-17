class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        unique = set()
        # Simpler solution:
        for num in nums:
            if num in unique:
                return num
            unique.add(num)

