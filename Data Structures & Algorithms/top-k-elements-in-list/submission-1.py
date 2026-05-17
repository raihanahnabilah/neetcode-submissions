class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1 -> put this in a map
        # check for the top K values with most 
        val_to_frequency = {}
        result = []
        for num in nums:
            if num in val_to_frequency:
                val_to_frequency[num] += 1
            else:
                val_to_frequency[num] = 1
        # print(sorted(val_to_frequency.items(), key=lambda x: x[1]))
        most_frequent = Counter(val_to_frequency).most_common(k)
        result = [e for (e,v) in most_frequent]

        return result

                

