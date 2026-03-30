class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash1 = {}
        arr = []
        for i in range(len(nums)):
            hash1[nums[i]] = 1 + hash1.get(nums[i],0)

        for i in range(k):
            max5 = 0
            mkey = 0 
            for j in hash1:
                if hash1[j] >= max5:
                    max5 = hash1[j]
                    mkey = j
            arr.append(mkey)    
            del hash1[mkey]
        return arr 
