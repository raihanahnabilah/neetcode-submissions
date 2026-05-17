class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        right = 0
        val_to_freq = {}

        res = 0

        while left <= right and left < len(s) and right < len(s):
            if s[right] not in val_to_freq:
                val_to_freq[s[right]] = 1
            else:
                val_to_freq[s[right]] += 1
            
            to_replace = ((right - left) + 1) - max(val_to_freq.values()) 
            if to_replace > k and left <= right and left < len(s):
                val_to_freq[s[left]] -= 1
                left += 1

            res = max(res, (right-left) + 1)
            right += 1

        return res

            
