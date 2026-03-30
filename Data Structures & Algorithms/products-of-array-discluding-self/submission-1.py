class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = []
        total = 1
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                total = nums[i] * total
            else:
                zero +=1
                continue
        for i in range(len(nums)):
            if zero == 1:
                if nums[i] != 0:
                    arr1.append(0)
                else:
                    arr1.append(total)
            elif zero > 1:
                arr1.append(0)
            else:
                arr1.append(total // nums[i])
        return arr1
