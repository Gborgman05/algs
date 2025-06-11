class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        hottest = []
        final = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if i == 0:
                hottest.append((i, temperatures[i]))
            else:
                while hottest and hottest[-1][1] < temperatures[i]:
                    index, temp = hottest.pop()
                    final[index] = i - index
                hottest.append((i, temperatures[i]))
        return final