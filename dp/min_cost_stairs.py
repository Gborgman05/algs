class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = []
        i = 0
        while i <= len(cost):
            if i < 2:
                min_cost.append(0)
            else:
                min_cost.append(min([min_cost[i-2] + cost[i-2], min_cost[i-1] + cost[i-1]]))
            i += 1
        return min_cost[-1]