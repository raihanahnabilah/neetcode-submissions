class KthLargest:

    # # Brute force: 
    # # Time complexity: O(m*nlogn)
    # # Space complexity: O(m) 

    # def __init__(self, k: int, nums: List[int]):
    #     # O(nlogn)
    #     self.array = nums
    #     self.k = k

    # def add(self, val: int) -> int:
    #     # Brute force - O(m*nlogn) -> m is the number of calls to add() and n is the number of elements added
    #     self.array.append(val)
    #     self.array = sorted(self.array, reverse=True)
    #     return self.array[self.k-1]
        
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        counter = len(self.minHeap) - self.k
        copyHeap = self.minHeap
        while counter > 0:
            heapq.heappop(copyHeap)
            counter -= 1
            
        return copyHeap[0]








