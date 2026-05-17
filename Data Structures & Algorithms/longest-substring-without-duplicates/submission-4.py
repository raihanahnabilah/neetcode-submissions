class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Method 1
        unique_chars_to_index = {}
        longest_substring = 0
        first_index = 0
        for i, char in enumerate(s):
            if char in unique_chars_to_index:
                # Case 1: abcb
                while s[first_index] != char and first_index < i:
                    del unique_chars_to_index[s[first_index]]
                    first_index += 1
                
                # Case 1 and 2: abca
                if s[first_index] == char:
                    first_index += 1

            unique_chars_to_index[char] = i

            if (i - first_index) + 1 > longest_substring:
                    longest_substring = (i - first_index) + 1
        return longest_substring


                



        