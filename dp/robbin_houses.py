class Solution:
    def rob(self, nums: List[int]) -> int:
        max_rob = []
        for num in nums:
            if len(max_rob) == 0:
                max_rob.append(num)
            elif len(max_rob) == 1:
                max_rob.append(max(max_rob[0], num))
            else:
                max_rob.append(max(max_rob[-1], max_rob[-2] + num))
        return max_rob[-1]