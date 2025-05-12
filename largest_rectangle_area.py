class Solution:
    # mostly learned from neetcode, unclear on ordering for some of this
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stck = [-1]
        for i in range(len(heights)):
            while stck[-1] != -1 and heights[i] <= heights[stck[-1]]:
                height = heights[stck.pop()]
                width = i - stck[-1] - 1
                max_area = max(max_area, height * width)
            stck.append(i)
        while stck[-1] != -1:
            height = heights[stck.pop()]
            width = len(heights) - stck[-1] - 1
            max_area = max(max_area, height * width)
        return max_area
        