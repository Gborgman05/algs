# Idea / Proof:

# The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
# All other containers are less wide and thus would need a higher water level in order to hold more water.
# The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.


O(n^2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)-1):
            for j in range(i, len(height)):
                tmp = (j - i) * min(height[i], height[j])
                if tmp > max_water:
                    max_water = tmp
        return max_water

O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        i = 0
        j = len(height) - 1
        while i < j:
            tmp = (j - i) * min(height[i], height[j])
            if tmp > max_water:
                max_water = tmp
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_water
