class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1,2,0,1,0

        # target: index 4
        # logic for bottom up, at any point, check if it's 4
        #   0
        #.      +1
        #.       1
        #.    +1  +2
        #     2.   3
        #    stuck +1
        #           4 
        # 4 is there, so we're good!

        # logic for top down
        #.        4
        #       index 4 = we dont care about the value
        #       index 3 + 1 =4 -> can reach 4, we're good
        #       index 2 + 0 = 2 -> cant reach 3, we're not good
        #       index 1 + 2 = 3 -> can reach 3, we're good
        #       index 0 + 1 = 1 -> can reach 1, we're good
        
        # time complexity: O(n)
        # space complexity: O(1)
        target_index = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= target_index:
                target_index = i
        
        return target_index == 0
            
                

