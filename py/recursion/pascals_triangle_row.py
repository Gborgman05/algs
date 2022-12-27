# returns a list representing that row in pascals triangle
# row index starts at 0 for [1]
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            prev = self.getRow(rowIndex - 1)
            summed = [1]
            for i in range(len(prev) - 1):
                summed.append(prev[i] + prev[i+1])
            summed.append(1)
            return summed
                
        