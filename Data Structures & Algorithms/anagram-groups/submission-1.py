class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1 = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key not in hash1:
                hash1[key] = []
            hash1[key].append(strs[i])
        return list(hash1.values())

            

            

           