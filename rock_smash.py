# Galen Borgman
# My solution to the Leetcode Problem located at https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3297/
import bisect
class Solution:
    # def combine_two()
    def lastStoneWeight(self, stones: List[int]) -> int:
        # my_stones = {}
        # for i in range(len(stones)):
        #     my_stones[stones[i]] = i
        # while(len(stones) > 1):
            # big = max(my_stones.keys())
            # # big = [my_stones[max(my_stones.keys())]]
            # big.insert(0, my_stones[big[0]])
            # del my_stones[big[0]]
            # small = max(my_stones.keys())
            # # big = [my_stones[max(my_stones.keys())]]
            # small.insert(0, my_stones[small[0]])
            # smashed = big[1] - small[1]
            # if smashed <= 0:
            #     pass
            # else:
        stones.sort()
        while(len(stones) > 1):
            print(stones)
            big = stones.pop()
            small = stones.pop()
            if big == small:
                pass
            else:
                bisect.insort(stones, big - small)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
