class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Lets sort the array
        # for-loop the array
        # -4, -1, -1, 0, 1, 2
        # -4, -1, 2 = -3 < less than 0 -> right + 1 doesnt work
        # -1, -1, 2 = 0 [Found]
        # -1, 0, 2 = 1 < more than 0 -> right - 1
        # -1, 0, 1 = 0 [Found]

        # Sort it
        nums.sort()

        res = []

        for i, num in enumerate(nums):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            currentVal = num
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] + currentVal == 0:
                    res.append([currentVal, nums[left], nums[right]])
                    # If there are more
                    left += 1
                    while right > left and nums[left] == nums[left-1]:
                        left += 1

                elif (nums[left] + nums[right] + currentVal) < 0:
                    left += 1
                elif (nums[left] + nums[right] + currentVal) > 0:
                    right -= 1
        
        return res

