class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashf = {}
        for i in range(len(nums)):
            sum = target - nums[i]
            if sum in hashf:
                return [hashf[sum], i]
            hashf[nums[i]] = i 
        return False
