class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean the string first and make it lower
        cleaned_string = [char.lower() for char in s if char.isalnum()]
        # cleaned_string = "".join(cleaned_string_arr)

        # then you wanna check if it's palindrome?
        left, right = 0, len(cleaned_string) - 1
        while left <= right:
            if cleaned_string[left] != cleaned_string[right]:
                return False
            left += 1
            right -= 1
            
        return True