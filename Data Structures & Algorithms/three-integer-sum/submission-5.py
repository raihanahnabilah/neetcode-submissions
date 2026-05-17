class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Using two pointers
        # The third pointer is the for-loop itself!

        # Sort this
        nums.sort()

        res = []

        for i, num in enumerate(nums):

            # to ensure there is no duplicates:
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums)-1

            while left < right:
                if num + nums[left] + nums[right] == 0:
                    res.append([num, nums[left], nums[right]])
                    # need to continue in case there are more?
                    left += 1
                    while right > left and nums[left] == nums[left-1]:
                        left += 1

                elif num + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
            
        return res



