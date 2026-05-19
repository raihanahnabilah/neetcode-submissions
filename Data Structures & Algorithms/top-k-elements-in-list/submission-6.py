class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # time complexity: O(k*n)
        # space complexity: O(n)

        num_to_frequency = {}
        for num in nums: # O(n)
            if num in num_to_frequency:
                num_to_frequency[num] += 1
            else:
                num_to_frequency[num] = 1

        res = []
        for _ in range(k): # O(k)
            curr_max = max(num_to_frequency, key=num_to_frequency.get)
            res.append(curr_max) # O(n)
            del num_to_frequency[curr_max]
        return res


            