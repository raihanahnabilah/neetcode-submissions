class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars_to_index = {}
        longest_substring = 0
        first_index = 0
        for i, char in enumerate(s):
            if char in unique_chars_to_index:
                print("I am here", char, unique_chars_to_index)
                # # store new first index
                # temp_first_index = unique_chars_to_index[char] + 1

                # Case 1: abcb
                while s[first_index] != char and first_index < i:
                    del unique_chars_to_index[s[first_index]]
                    first_index += 1
                
                # Case 1 and 2: abca
                if s[first_index] == char:
                    first_index += 1

                # first_index = temp_first_index

                # update first_index
                unique_chars_to_index[char] = i
                print("I am here after", char, unique_chars_to_index, first_index)
            else:
                print("I am in else", char, unique_chars_to_index)
                unique_chars_to_index[char] = i
            if (i - first_index) + 1 > longest_substring:
                    longest_substring = (i - first_index) + 1
        return longest_substring


                



        