class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lili = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i != 0:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum1 = nums[i] + nums[l] + nums[r]
                if sum1 > 0:
                    r -=1
                elif sum1 < 0:
                    l +=1
                else:
                    lili.append([nums[i],nums[l],nums[r]])
                    l +=1
                    while l < r and nums[l] == nums[l - 1]:
                        l +=1
        return lili