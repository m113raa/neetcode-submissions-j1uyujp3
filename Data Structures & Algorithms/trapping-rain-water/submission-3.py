class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxR = height[r] # 1 -> 2 -> 3 
        maxL = height[l] # 0 -> 2 ->3
        total = 0 #2 -> 4 - >7
        while l < r :
            if maxL < maxR: # maxl = 3 , maxr = 3
                l += 1 #l = 3
                maxL = max(maxL, height[l]) #(0,2) -> 2 / (2, 0) -> 2 / (2, 3) -> 3
                total += maxL - height[l] # 0 = 2 - 2 -> 0 / (2- 0) = 2 / 2 =(3 -3) -> 2

            else:
                r -= 1 #r = 8 / r = 7 / r = 6 / r = 5 / r =4
                maxR = max(maxR, height[r]) #(1, 2) ->2 / (2, 3) -> 3 /(3, 1) -> 3 / (3, 0) - > 3 /
                total += maxR - height[r] # 0 = 2 - 2 -> 0 / 0 = 3 - 3  / 2 = (3 - 1) ->2+2 = 4 / 4 = (3,0) -> 7
        return total