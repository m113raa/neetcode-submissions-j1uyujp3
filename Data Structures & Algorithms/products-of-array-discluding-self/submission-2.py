class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lili = []
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
                    lili.append(0)
                else:
                    lili.append(total)
            elif zero > 1:
                lili.append(0)
            else:
                lili.append(total // nums[i])
        return lili

