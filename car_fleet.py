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

        
        class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # find the time that they combine?
        # find the time they reach the position

        time_reached = [0] *len(position)
        combined = sorted([ (position[i], speed[i]) for i in range(len(position))], key=lambda x:x[0])[::-1]
        #print(combined)
        final = []
        for i in range(len(combined)):
            time = (target - combined[i][0]) / combined[i][1]
            #print(final)
            if not final or final[-1] < time:
                final.append(time)
        return len(final)
