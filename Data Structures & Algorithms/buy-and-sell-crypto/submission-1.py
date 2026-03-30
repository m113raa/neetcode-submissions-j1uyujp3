class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        temp = prices[0]
        for i in range(len(prices)):
            if prices[i] < temp :
                temp = prices[i] 
            elif  prices[i] > temp:
                max1= prices[i] - temp
                profit = max(max1, profit)
        return profit