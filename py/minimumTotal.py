class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_cost = []
        for i in range(len(triangle)):
            row = []
            for j in range(len(triangle[i])):
                if i == 0:
                    row.append(triangle[i][j])
                else:
                    if j > 0 and j < len(triangle[i]) - 1:
                        row.append(min(min_cost[i-1][j-1], min_cost[i-1][j]) + triangle[i][j])
                    if j == 0:
                        print(i)
                        print(min_cost)
                        print(j)
                        triangle[i][j]
                        row.append(min_cost[i-1][j] + triangle[i][j])
                    if j == len(triangle[i]) - 1:
                        row.append(min_cost[i-1][j-1]+ triangle[i][j])
            min_cost.append(row)
        return min(min_cost[-1])