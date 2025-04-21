class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        min_pos = min(position)
        comb = [[position[i], speed[i]] for i in range(len(position))]
        comb = sorted(comb, key=lambda a: a[0])
        cur = final = 0
        times = [(target - car[0]) / car[1] for car in comb]
        i = -1
        while i > -len(times) - 1:
            if cur < times[i]:
                final += 1
                cur = times[i]
            i -= 1
        return final

        