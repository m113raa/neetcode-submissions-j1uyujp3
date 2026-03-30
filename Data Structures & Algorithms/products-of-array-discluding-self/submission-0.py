class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lili = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            lili[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1 , -1):
            lili[i] *= post
            post *= nums[i]
        return lili