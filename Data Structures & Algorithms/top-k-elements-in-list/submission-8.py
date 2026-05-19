class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # # solution 1
        # # time complexity: O(k*n)
        # # space complexity: O(n)

        # num_to_frequency = {}
        # for num in nums: # O(n)
        #     if num in num_to_frequency:
        #         num_to_frequency[num] += 1
        #     else:
        #         num_to_frequency[num] = 1

        # # .items (for key-value), .get (for key), .values (for value)
        # res = []
        # for _ in range(k): # O(k)
        #     curr_max_key, curr_max_val = max(num_to_frequency.items(), key=lambda row: row[1])
        #     res.append(curr_max_key) # O(n)
        #     del num_to_frequency[curr_max_key]
        # return res


        # solution 2:
        # time complexity: O(n)
        # space complexity: O(n) -> length of nums

        num_to_frequency = {}
        for num in nums: # O(n)
            if num in num_to_frequency:
                num_to_frequency[num] += 1
            else:
                num_to_frequency[num] = 1

        # key: 1 -> freq: 1
        # key: 2 -> freq: 3
        # to get bucket
        max_frequency = max(num_to_frequency.values()) # O(n)
        max_frequency_bucket = [[] for _ in range(max_frequency + 1)]

        print(num_to_frequency.items())
        # [[],[1],[],[2]]
        # to place these in a bucket:
        for key, freq in num_to_frequency.items():
            max_frequency_bucket[freq].append(key)

    
        res = []
        counter = k
        for i in range(len(max_frequency_bucket)-1, -1, -1): # O(n)
            if len(res) == k:
                break
            if len(max_frequency_bucket[i]) <= 0:
                continue
            if len(max_frequency_bucket[i]) >= counter:
                res.extend(max_frequency_bucket[i][:k])
                counter -= len(max_frequency_bucket[i][:k])
            else:
                res.extend(max_frequency_bucket[i])
                counter -= len(max_frequency_bucket[i])
        return res





            