class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) -1
        min1 = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                min1 = min(min1, nums[l])
                break
            mid = (l + r) // 2
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            min1 = min(min1 , nums[mid])
            
        return min1

            
            


