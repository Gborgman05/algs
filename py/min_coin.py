class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        store = {}
        for i in range(amount + 1):
            if i == 0:
                store[i] = 0
            else:
                poss = []
                for coin in coins:
                    if i - coin >= 0 and store[i - coin] != -1:
                        poss.append(store[i - coin])
                if not poss:
                    store[i] = -1
                else:
                    store[i] = min(poss) + 1
                # if i > 25:
                #     store[i] = min(store[i-1], store[i - 5], store[i - 10], store[i - 25]) + 1
                # elif i > 10:
                #     store[i] = min(store[i-1], store[i - 5], store[i - 10]) + 1
                # elif i > 5:
                #     store[i] = min(store[i-1], store[i -5]) + 1
                # else:
                #     store[i] = store[i-1] + 1
        print(store)
        return store[amount]