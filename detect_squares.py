class DetectSquares:

    def __init__(self):
        self.x_points = {}
        self.y_points = {}
        

    def add(self, point: List[int]) -> None:
        if point[0] in self.x_points:
            self.x_points[point[0]].append(point)
        else:
            self.x_points[point[0]] = [point]
        if point[1] in self.y_points:
            self.y_points[point[1]].append(point)
        else:
            self.y_points[point[1]] =[point]


    def count(self, point: List[int]) -> int:
        if point[0] in self.x_points
            points_left = self.x_points[point[0]]
        else:
            return 0
        if point[1] in self.y_points:
            points_down = self.y_points[point[1]]
        else:
            return 0
        for i in range(len(points_left)):
            # check there are two equidistant points (below and diagonal)
            y_diff = point[1] - points_left[i][1]
            for j in range(len(points_down)):
                if points_down[j][1] == points_left[i][1]:
                    # two points
                    if points_down[j][0] in self.x_points
                        dia_points_left = self.x_points[point[0]]
                        dia_points = [x for x in dia_points_left if x[]]
                    if points_left[i][1] in self.y_points:
                        dia_points_down = self.y_points[point[1]]
                
            req_points
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)