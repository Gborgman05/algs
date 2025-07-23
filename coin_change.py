class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_count = [-1] * (amount + 1)
        coin_count[0] = 0
        for i in range(len(coin_count)):
            poss_counts = [coin_count[i - coin] + 1 for coin in coins if i - coin >= 0 and coin_count[i-coin] != -1]
            if poss_counts:
                coin_count[i] = min(poss_counts)
        return coin_count[-1]
