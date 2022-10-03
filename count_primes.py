class Solution:
    def countPrimes(self, n: int) -> int:
        composite = {}
        primes = []
        for i in range(2, n):
            if i in composite:
                pass
            else:
                primes.append(i)
                for j in range(i, n, i):
                    composite[j] = True
        # print(composite)
        return len(primes)