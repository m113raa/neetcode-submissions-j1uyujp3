class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash1 = {}
        for i in range(len(nums)):
            if nums[i] in hash1:
                return True
            hash1[nums[i]] = i
        return False
