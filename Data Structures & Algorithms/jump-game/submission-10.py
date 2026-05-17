class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        last_index = len(nums) - 1

        for i, num in enumerate(nums):
            if i > max_reach:
                return False # this means we cant even reach it
            
            max_reach = max(max_reach, i + num)
        
            if max_reach >= last_index:
                return True
        
        return True


        