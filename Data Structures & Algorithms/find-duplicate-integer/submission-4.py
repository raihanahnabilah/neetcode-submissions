class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # # Time complexity: O(n)
        # # Space complexity: O(k)
        # unique = set() # This is O(k) k being unique numbers
        # # Simpler solution:
        # for num in nums: # This is O(n)
        #     if num in unique:
        #         return num
        #     unique.add(num)


        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1
        
        return -1

