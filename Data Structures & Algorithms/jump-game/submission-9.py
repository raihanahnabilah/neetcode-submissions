class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # # back to front
        # target = len(nums) - 1
        # for i in range(len(nums)-2, -1,-1):
        #     if i + nums[i] >= target:
        #         target = i
            
        # return target == 0

        # front to back
        highest = 0
        target = len(nums) - 1
        for i in range(len(nums)-1):
            print(highest, target, i, nums[i])
            if highest < i:
                return False

            highest = max(highest, i + nums[i])

            if highest >= target:
                print("checking target highest", target, highest)
                return True
        
        return highest >= target
            





