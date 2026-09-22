class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                print(buy)
                continue
            profit = max(profit, (prices[i] - buy))
        
        return profit
            