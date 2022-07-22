class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lcal_min = 0
        profit = []
        for i in range(len(prices)):
            if prices[i] < prices[lcal_min]:
                lcal_min = i
            profit.append(prices[i] - prices[lcal_min])
        return max(profit)    
            
            