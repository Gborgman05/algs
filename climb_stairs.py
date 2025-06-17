class Solution:
    def climbStairs(self, n: int) -> int:
        items = [1, 2]
        while len(items) < n:
            items.append(items[-1] + items[-2])
        return items[n -1]
    

    class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        stairs = [0] * n
        stairs[0] = 1
        stairs[1] = 2
        for i in range(2, n):
            stairs[i] = stairs[i-1] + stairs[i-2]
        return stairs[-1]

        