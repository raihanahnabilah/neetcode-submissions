class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # # time complexity: O(n^3logn)
        # array_length = len(stones)
        # while array_length > 1:
        #     heap_stones = []
        #     for stone in stones:
        #         heapq.heappush(heap_stones, stone)
        #         if len(heap_stones) > 2:
        #             heapq.heappop(heap_stones)

        #     if heap_stones[0] != heap_stones[1]:
        #         stones.append(abs(heap_stones[0] - heap_stones[1]))
        #         array_length += 1

        #     stones.remove(heap_stones[0])
        #     stones.remove(heap_stones[1])
        #     array_length -= 2

        # return stones[0] if stones else 0


        stones = [-stone for stone in stones]
        # heapify it
        heapq.heapify(stones)

        while len(stones) > 1:
            # pop the values
            val1 = heapq.heappop(stones) # most negative
            val2 = heapq.heappop(stones) # most negative

            print("checking stones before", stones)

            if abs(val1) != abs(val2):
                heapq.heappush(stones, - abs(val1 - val2))
            
        
        return -stones[0] if stones else 0



        

