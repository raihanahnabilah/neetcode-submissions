class Solution:
    def findMin(self, nums: List[int]) -> int:
        # i know the answer after looking at hints
        left = 0
        right = len(nums) - 1

        if len(nums) < 2:
            return nums[0]

        # if it's already sorted
        if nums[left] < nums[right]:
            return nums[left]
        
        while left < right:
            middle = (left + right) // 2
            # edges:
            if middle == left or middle == right:
                if nums[left] < nums[right]:
                    return nums[left]
                else:
                    return nums[right]
            
            if nums[middle-1] > nums[middle] and nums[middle] < nums[middle+1]:
                # print("return")
                return nums[middle]
            if nums[left] < nums[middle]:
                left = middle
                print("new left", left)
                print("right", right)
            else:
                right = middle
                print("new right", right)
                print("left", left)

        return -1


            

            
            

