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
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy, sell, skip
        max_amt = 0

        dp = {}
        def helper(index, is_buying):
            if (index, is_buying) in dp:
                return dp[(index, is_buying)]
            if index >= len(prices): 
                return 0
            cooldown = helper(index + 1, is_buying)

            if is_buying:
                buy = helper(index + 1, not is_buying) - prices[index]
                dp[(index, is_buying)] = max(cooldown, buy)
            else:
                sell = helper(index + 2, not is_buying) + prices[index]
                dp[(index, is_buying)] = max(cooldown, sell)
            return dp[(index, is_buying)]
        return helper(0, True)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_poss = prices[0]
        max_poss = 0
        for price in prices:
            if price < min_poss:
                min_poss = price
            else:
                max_poss = max(max_poss, price - min_poss)
        return max_poss
