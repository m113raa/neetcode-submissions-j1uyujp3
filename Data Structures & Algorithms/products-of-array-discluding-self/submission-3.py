class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mimi = []
        pro = 1
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter +=1
                continue
            pro *= nums[i]
        if counter == 0:
            for i in range(len(nums)):
                mimi.append(pro // nums[i])
        elif counter == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    mimi.append(pro)
                else:
                    mimi.append(0)
        else:
            mimi=[0] *len(nums)
        return mimi