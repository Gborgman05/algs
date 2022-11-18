class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xb, yb, ans = f'{x:032b}', f'{y:032b}', 0
        return sum(i != j for i, j in zip(xb, yb))
#         x = str(bin(x))[2:]
#         y = str(bin(y))[2:]

#         print(x, " ", y)
#         cnt = cnt2 = -1
#         dist = 0
#         if max(len(x), len(y)) < 4:
#             dist += 4 - max(len(x), len(y))
#         while len(x) > abs(cnt) - 1 and len(y) > abs(cnt) - 1:
#             if x[cnt] == y[cnt]:
#                 pass
#             else:
#                 dist += 1
#             cnt -= 1
#         while len(x) > abs(cnt) - 1:
#             if x[cnt] == 1:
#                 dist += 1
#             cnt -= 1
#         while len(y) > abs(cnt) - 1:
#             if y[cnt] == 1:
#                 dist += 1
#             cnt -= 1
#         return dist