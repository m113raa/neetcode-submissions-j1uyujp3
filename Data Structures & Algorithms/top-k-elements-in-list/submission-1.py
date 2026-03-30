class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1 ={}
        arr =[]
        for i in range(len(nums)):
            hash1[nums[i]] = 1 + hash1.get(nums[i], 0)

        for i in range(k):
            max1 = 0
            key = 0
            for j in hash1:
                if hash1[j] > max1:
                    max1 = hash1[j]
                    key = j
            arr.append(key)
            del hash1[key]
            
        return arr