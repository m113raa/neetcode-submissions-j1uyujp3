class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        hashmap1 = {}
        res = 0
        for r in range(len(s)):
            if s[r] in hashmap1:
                l = max(l, hashmap1[s[r]]+1)
            hashmap1[s[r]] = r
            res = max(res, r - l + 1 )
        return res
        