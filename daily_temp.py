#O(n^2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in temperatures]
        for i in range(len(temperatures) - 1, -1, -1):
            if i==len(temperatures)-1:
                pass
            else:
                for j in range(len(temperatures)-i):
                    if temperatures[i + j] > temperatures[i]:
                        answer[i] = j
                        break
        return answer
#better in average case, but still O(n^2) in worst case

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in temperatures]
        for i in range(len(temperatures) - 1, -1, -1):
            if i==len(temperatures)-1:
                pass
            else:
                j = 1
                while j + i < len(temperatures):
                    #check this one
                    if temperatures[j+i] > temperatures[i]:
                        answer[i] = j
                        break
                    else:
                        if answer[j+i] == 0:
                            answer[i] = 0
                            break
                        else:
                            j += answer[j+i]

        return answer