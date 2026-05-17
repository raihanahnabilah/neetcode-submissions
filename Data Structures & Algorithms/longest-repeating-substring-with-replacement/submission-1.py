class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       
       # we have the right pointer
       # it's valid if our current window size (r-l + 1) - max_freq <= k:
       # else, we wanna move left pointer

        left = 0
        right = 0
        hashMap = {}
        res = 0
        while left <= right and right < len(s):
            if s[right] in hashMap:
                hashMap[s[right]] += 1
            else:
                hashMap[s[right]] = 1
        
            max_freq = max(hashMap.values())

            if (right - left + 1) - max_freq > k:
                # remove prev left
                hashMap[s[left]] -= 1
                if hashMap[s[left]] == 0:
                    del hashMap[s[left]]
                # increment left
                left += 1
            
            res = max(res, right - left + 1)
            right += 1

        return res
            
        
