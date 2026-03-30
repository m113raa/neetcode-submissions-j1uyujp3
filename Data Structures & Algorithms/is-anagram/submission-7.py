class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hash1[s[i]] = 1 + hash1.get(s[i], 0)
            hash2[t[i]] = 1 + hash2.get(t[i], 0)
        for char in hash1:
            if hash1[char] != hash2.get(char, 0):
                return False
        return True

