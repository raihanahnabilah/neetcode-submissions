class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # O(n^3)
        # # sort them in asc -> -4,-1,-1,0,1,2,
        # # 0 > -6
        # # move up all pointers: 0 > 0
        
        # # -5, -2, -1, 1, 3
        # # 0
        # # 0
        # # step 1: sort the array
        # nums.sort()
        # # step 2: traverse through the array, add two numbers together, put them in a map
        # sum_of_two_to_original_numbers = {}
        # for i, num in enumerate(nums):
        #     if i == 0:
        #         continue
        #     sum_of_two = num + nums[i-1]
        #     sum_of_two_to_original_numbers[sum_of_two] = [nums[i-1], num]

        # # step 3: traverse through the array again
        # result = []
        # unique_result = set()
        # for i, num in enumerate(nums):
        #     sum_of_two_required = 0 - num
        #     if sum_of_two_required in sum_of_two_to_original_numbers:
        #         temp_result = sum_of_two_to_original_numbers[sum_of_two_required].copy()
        #         temp_result.append(num)
        #         temp_result.sort()
        #         if "".join([str(item) for item in temp_result]) in unique_result:
        #             continue 
        #         unique_result.add("".join([str(item) for item in temp_result]))
        #         result.append(temp_result)
        #         temp_result = []
        
        # # Step 4: Remove non duplicates 

        # return result

        # The correct method (after looking at Neetcode):
        # sort the array, that part is already correct:
        nums.sort()
        print("sorted nums:", nums)

        # traverse through the array, if the value is the same as previous one, you wanna skip
        result = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            left_pointer = i + 1
            right_pointer = len(nums) - 1
            while left_pointer < right_pointer:
                if num + nums[left_pointer] + nums[right_pointer] == 0:
                    result.append([num, nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    # BUT tricky condition with cases like [-2, 0,0, 2,2]
                    while nums[left_pointer] == nums[left_pointer-1] and right_pointer > left_pointer:
                        left_pointer += 1

                    
                elif num + nums[left_pointer] + nums[right_pointer] < 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return result
                    
                    
                
    





            







    