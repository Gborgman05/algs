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


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        ans = [0] * len(temperatures)
        max_temp = 0
        for i in range(len(temperatures)):
            while stack and  temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = (i - stack[-1])
                stack.pop()
            stack.append(i)
        return ans
