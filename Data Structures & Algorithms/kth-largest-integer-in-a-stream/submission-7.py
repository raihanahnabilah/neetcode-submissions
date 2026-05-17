class KthLargest:

    # time complexity: O(n)
    # space complexity: O(k)

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap) # O(n)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val) # O(logk)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0] # O(1)
