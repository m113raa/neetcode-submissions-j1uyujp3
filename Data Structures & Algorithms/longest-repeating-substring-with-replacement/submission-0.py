class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
         l = 0
         res =  0
         hash1 = {}
         max1 = 0
         for r in range(len(s)):
            hash1[s[r]] = 1 + hash1.get(s[r], 0)
            max1 = max(max1, hash1[s[r]])

            while (r - l + 1) - max1 > k:
                hash1[s[l]] -=1
                l +=1
            res = max(res, r - l + 1)
         return res

