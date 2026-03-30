class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(1, len(prices)):
            if (prices[r] - prices[l]) <= 0: # 2 - 1 / 1 - 1 / 0 - 1 / 1 -0 / 2 -0
                l +=1 # 1 , 2 , 3, 4
                if res != 0:
                    l = r # l = 4, r = 4
                continue
            else:
                res = max(res, prices[r]- prices[l]) # 1 
        return res
        