class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # [-1, 0, 1, 2, -1, -4]

        # # brute force solution
        # res = set()
        # nums.sort()

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                  res.add(tuple([nums[i], nums[j], nums[k]]))
                         
        # return [list(i) for i in res]

        # the more optimized solution
        # [-4,-1,-1,0,1,2]
        res = set()
        nums.sort() # sort first

        for i, num in enumerate(nums):
            left_pointer = i + 1
            right_pointer = len(nums) - 1
            target = 0 - num

            while left_pointer < right_pointer:
                if nums[left_pointer] + nums[right_pointer] == target:
                    res.add(tuple([num, nums[left_pointer], nums[right_pointer]])) 
                    # for edge cases such as
                    # [-3,-1,0,0,1,1,2,3]
                    left_pointer += 1
                    right_pointer -= 1
                    while left_pointer < len(nums) and nums[left_pointer-1] == nums[left_pointer]:
                        left_pointer += 1
                    while right_pointer >= 0 and nums[right_pointer+1] == nums[right_pointer]:
                        right_pointer -= 1
                elif nums[left_pointer] + nums[right_pointer] <= target:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return [list(i) for i in res]



