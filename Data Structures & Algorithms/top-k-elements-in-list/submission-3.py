class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # two ways:
        # (1) hash map -> value to frequency
        #     return the hashmap value in decreasing frequency
        # (2) array of values that has [0] * 9 -> but this will be O(n)

        # method 1:
        # time complexity: O(mlogm), m is the unique values in the nums
        # space complexity: O(m), m is the unique values in the nums
        value_to_frequency = {}
        for num in nums:
            if num in value_to_frequency:
                value_to_frequency[num] += 1
            else:
                value_to_frequency[num] = 1

        sorted_hash_map = sorted(value_to_frequency.items(), key=lambda item: item[1], reverse=True)
        return [key for key, val in sorted_hash_map[:k]]
