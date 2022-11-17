# class Solution:
#     def countPrimes(self, n: int) -> int:
#         composite = {}
#         primes = []
#         for i in range(2, n):
#             if i in composite:
#                 pass
#             else:
#                 primes.append(i)
#                 for j in range(i, n, i):
#                     composite[j] = True
#         # print(composite)
#         return len(primes)
# class Solution:
class Solution:
    def countPrimes(self, n: int) -> int:
        seen, ans = [0] * n, 0
        for num in range(2, n):
            if seen[num]: continue
            ans += 1
            seen[num*num:n:num] = [1] * ((n - 1) // num - num + 1)
        return ans
#     def countPrimes(self, n: int) -> int:
#         marked = {key : 0 for key in range(2, n)}
#         count = n
#         for i in range(2, n):
#             if marked[i] == 1:
#                 continue
#             start = i * i
#             for j in range(start, n, i):
#                 if not marked[j]:
#                     marked[j] = 1
#                     count -= 1
#         return n - count
            
