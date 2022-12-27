# solution to fibonnaci using memoization to limit number of calculations at cost of RAM
class Solution:
    def fib(self, n: int) -> int:
        store = {}
        def fib_recursive(n):
            if n in store:
                return store[n]
            elif n < 2:
                return n
            else:
                new = fib_recursive(n-1) + fib_recursive(n-2)
                store[n] = new
                # print(store)
                return new
        return fib_recursive(n)
        