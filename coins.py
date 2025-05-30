class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins_for_amount = [0] * (amount + 1)
        for i in range(len(coins_for_amount)):
            poss = [coins_for_amount[i-coin] + 1 for coin in coins if i-coin >=0 and (coins_for_amount[i-coin] != 0 or i-coin ==0)]
            if poss:
                coins_for_amount[i] = min(poss)
        #print(coins_for_amount)
        if coins_for_amount[-1] == 0:
            return -1
        else:
            return coins_for_amount[-1]