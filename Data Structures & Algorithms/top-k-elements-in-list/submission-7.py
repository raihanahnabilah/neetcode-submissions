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

        # .items (for key-value), .get (for key), .values (for value)
        res = []
        for _ in range(k): # O(k)
            curr_max_key, curr_max_val = max(num_to_frequency.items(), key=lambda row: row[1])
            res.append(curr_max_key) # O(n)
            del num_to_frequency[curr_max_key]
        return res


            