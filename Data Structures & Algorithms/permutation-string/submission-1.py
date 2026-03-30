class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1 = {} # {a:1, b:1, c:1}
        hashmap2 = {} # {e:1, c:1, a:1}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            hashmap1[s1[i]] = 1 + hashmap1.get(s1[i], 0) 
            hashmap2[s2[i]] = 1 + hashmap2.get(s2[i], 0)

        if hashmap1 == hashmap2:
            return True
        
        l = 0  
        for r in range(len(s1), len(s2)):
            hashmap2[s2[r]] = 1 + hashmap2.get(s2[r], 0)
            if hashmap2[s2[l]] > 1:
                hashmap2[s2[l]] -=1
            elif hashmap2[s2[l]] == 1:
                del hashmap2[s2[l]]
            l +=1
            if hashmap1 == hashmap2:
                return True
        return False
        

            