class Solution:
    # could use input array to reduce time and space used
    def minCosts(self, cost: List[int]) -> List[int]:
        final = []
        min_front = cost[0]
        for c in cost:
            if min_front > c:
                final.append(c)
                min_front = c
            else:
                final.append(min_front)
        return final