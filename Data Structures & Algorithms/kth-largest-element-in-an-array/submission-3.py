class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums: [1,2,3,4]
        # k: 2

        # the easy solution:
        nums.sort(reverse = True) #in-memory sort
        
        return nums[k-1]
