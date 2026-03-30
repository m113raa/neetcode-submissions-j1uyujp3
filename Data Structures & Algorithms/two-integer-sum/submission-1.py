class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hashMap = {}
      for i in range(len(nums)):
            star = target - nums[i]
            if star in hashMap:
                return [hashMap[star], i]
            hashMap[nums[i]] = i
      return False
