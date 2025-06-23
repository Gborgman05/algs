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


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        max_prof = 0
        for i in range(len(prices)):
            if prices[i] > low:
                max_prof = max(max_prof, prices[i] - low)
            else:
                low = prices[i]
        return max_prof
        