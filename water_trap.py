class Solution:
    def trap(self, height: List[int]) -> int:
        # go until you find the next height level, then record depth at each column you pass
        l = 0
        r = len(height) - 1
        l_height, r_height = 0, 0
        total_vol = 0
        min_height = 0
        while l < r:
            # find leftmost increase
            if l_height <= r_height:
                while l < r and height[l] <= l_height:
                    total_vol += max(min_height - height[l], 0)
                    l += 1
                l_height = height[l]
                min_height = min(l_height, r_height)
            else:
                while l < r and height[r] <= r_height:
                    total_vol += max(min_height - height[r], 0)
                    r -= 1
                r_height = height[r]
                min_height = min(l_height, r_height)
        return total_vol
            
