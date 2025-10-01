class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        rem = 0
        while numBottles > 0:
            # print(numBottles)
            # print(rem)
            res += numBottles
            empty = numBottles + rem
            refilled = math.floor((numBottles + rem) / numExchange)
            rem = numBottles + rem - (refilled * numExchange)
            numBottles = refilled
        return res
