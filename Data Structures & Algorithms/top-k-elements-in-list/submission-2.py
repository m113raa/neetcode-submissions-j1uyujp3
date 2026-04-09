class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mimi = []
        hash1= {}
        for i in range(len(nums)):
            hash1[nums[i]] = 1 + hash1.get(nums[i], 0)

        for i in range(k):
            res = 0 
            maxKey = 0
            for key in hash1:
                if hash1[key] > res:
                    res = hash1[key]
                    maxKey = key
            mimi.append(maxKey)
            del hash1[maxKey]
        return mimi
