# Created by gbrgm on 10/21/2020
# Title: coin problem

class max_coin_problem:
    def __init__(self, coins):
        self.coins = [0] + coins
        self.solutions = [0] + [None] * len(coins)

    def solve(self, index=None):
        if index is None:
            index = len(self.coins) - 1
        if self.solutions[index] is not None:
            return self.solutions[index]
        elif index < 2:
            return max(self.coins[0], self.coins[1])
        else:
            solution = max(self.coins[index] + self.solve(index - 2),
                           self.solve(index - 1))
            self.solutions[index] = solution
            return solution


if __name__ == "__main__":
    coin_problem = max_coin_problem([5, 1, 2, 10, 6, 3])
    print(coin_problem.solve())
