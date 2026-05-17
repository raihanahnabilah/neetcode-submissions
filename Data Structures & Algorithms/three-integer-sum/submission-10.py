class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
    # [-4, -1, -1, 0, 1, 2]
    
    # Brute force method:
    # For loop i, j, k
    # -4, -1, -1
    # -4, -1, 0
    # -4, -1, 1 -> etc

    # Non-brute force method
    # -4 + (-1) = -5 -> check in the set if we have 5
    # have a pointer at the very end -> 2 
    # -5 + 2 = -3 -> < 0? so we need to move our left pointers

    # -1 + -1 = -2 -> check at the very end -> 2
    # -2 + 2 = 0, good. next step

    # -1 + 0 = -1 -> check at the very end -> 2
    # -1 + 2 > 0, so we need to move our right pointer
    
    # -1 + 0 = -1 -> check at the very end -> 1
    # -1 + 1 = 0, good. next step

    # -1 is the same as previous -1 -> so need to increase our left pointer

    # 0 + 1 = 1 -> we cant do this anymore because it's equal already
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue # skip to the next one

            left, right = i + 1, len(nums) - 1

            while left < right:
                if num + nums[left] + nums[right] == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                    
                elif num + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
                
        return res




        








