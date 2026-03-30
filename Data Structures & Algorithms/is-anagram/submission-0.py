class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if range(len(s)) != range(len(t)):
            return False

        Shashmap = {}
        Thashmap = {}
        for i in range(len(s)):
            Shashmap[s[i]] = 1 + Shashmap.get(s[i], 0)
            Thashmap[t[i]] = 1 + Thashmap.get(t[i], 0)
        for n in s:
            if Shashmap[n] != Thashmap.get(n, 0):
                return False
        return True
