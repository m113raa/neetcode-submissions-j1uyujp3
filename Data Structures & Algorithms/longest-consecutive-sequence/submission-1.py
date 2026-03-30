class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        hash1 = {}
        max1 = 0
        for n in nums:
            length = 0
            if n-1 not in numset:
                hash1[n] = []
                while n + length in numset:
                    hash1[n].append(n + length)
                    length += 1
                max1 = max(length, max1)
            
        return max1
            
