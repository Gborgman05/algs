class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cumulative = [0] * (len(cost) + 1)
        for i in range(2, len(cost)+ 1):
            cumulative[i] = min(cost[i-1] + cumulative[i-1], cost[i-2] + cumulative[i-2])
        #print(cumulative)
        return cumulative[-1] 