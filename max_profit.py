class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        mini = prices[0]
        maxi = prices[0]
        for price in prices:
            if price > mini:
                prof = max(prof, price - mini)
            if price < mini:
                mini = price
        return prof
