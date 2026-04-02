class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        hash1 = {}
        res = 0
        for r in range(len(s)):
            while s[r] in hash1:
                del hash1[s[l]]
                l +=1
            hash1[s[r]] = r
            res = max(res, r-l+1)
        return res