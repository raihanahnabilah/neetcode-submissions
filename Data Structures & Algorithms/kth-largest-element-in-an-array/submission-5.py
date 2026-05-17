class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # heapify! this is min heap
        heapq.heapify(nums)
        print(nums)

        num_of_heapify_pop = len(nums) - k
        for i in range(num_of_heapify_pop):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)


        