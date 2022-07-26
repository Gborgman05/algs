# optimized for space 99.7% not speed
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        to_fill = []
        to_fill.append((sr, sc))
        cur_color = image[sr][sc]
        filled = {}
        while to_fill:
            curr = to_fill.pop(0)
            if curr[0] - 1 >= 0 and (curr[0] - 1, curr[1]) not in filled and image[curr[0] - 1][curr[1]] == cur_color:
                to_fill.append((curr[0] - 1, curr[1]))
            if curr[1] - 1 >= 0 and (curr[0], curr[1] - 1) not in filled and image[curr[0]][curr[1] - 1] == cur_color:
                to_fill.append((curr[0] , curr[1] - 1))
            if curr[0] + 1 < len(image) and (curr[0] + 1, curr[1]) not in filled and image[curr[0] + 1][curr[1]] == cur_color:
                to_fill.append((curr[0] + 1, curr[1]))
            if curr[1] + 1 < len(image[0]) and (curr[0], curr[1] + 1) not in filled and image[curr[0] ][curr[1] + 1] == cur_color:
                to_fill.append((curr[0] , curr[1] + 1))
            image[curr[0]][curr[1]] =color
            filled[curr] = 0
            
        return image
                
        
        