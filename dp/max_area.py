class Solution:
    def maxArea(self, height: List[int]) -> int:
        best_left = 0
        highest = 0
        i = 0 
        j = len(height) - 1
        while i < j:
            vol = (j - i) * min(height[i], height[j])
            if vol > highest:
                highest = vol
            if height[i] > height[j]:
                j -= 1
            elif height[i] <= height[j]:
                i += 1
        return highest
                
            