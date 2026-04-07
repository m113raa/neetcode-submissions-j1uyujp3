class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash1 = {}
        setN = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i]-1 not in setN:
                hash1[nums[i]] = 1 + hash1.get(nums[i], 0)
                length = 1
                while nums[i]+length in setN:
                    length +=1
                    hash1[nums[i]] = 1 + hash1.get(nums[i], 0)
                longest = max(longest, length)
        return longest
                    

                    
