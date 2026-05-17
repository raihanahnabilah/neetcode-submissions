class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums: [1,2,3,4]
        # k: 2

        # # time complexity: O(nlogn)
        # # the easy solution:
        # nums.sort(reverse = True) #in-memory sort
        # return nums[k-1]

        # Heap:
        # kth largest element
        # 1,2,3,4,5,6 kth 2 largest element
        # 5
        # min heap of size 2, take the smallest one
        fixed_heap = []

        for num in nums:
            heapq.heappush(fixed_heap, num)
            if len(fixed_heap) > k:
                heapq.heappop(fixed_heap)
            
        return heapq.heappop(fixed_heap)






