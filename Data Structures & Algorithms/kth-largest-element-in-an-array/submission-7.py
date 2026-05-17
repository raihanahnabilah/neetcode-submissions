class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time complexity: O(nlogn)
        # space complexity: O(1)

        heapq.heapify(nums) # O(n)
        while len(nums) > k: # O(n)
            heapq.heappop(nums) # O(logn)
        return nums[0]
