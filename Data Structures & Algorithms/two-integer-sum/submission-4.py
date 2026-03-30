class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}
        for i in range(len(nums)):
            sum1 = target - nums[i]
            if sum1 in hash1:
                return [hash1[sum1], i]
            hash1[nums[i]] = i
        return False

