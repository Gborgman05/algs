class matrix:

    def __init__(self, nums):
        self.rows = []
        self.vector = []
        nums = nums.split(' ')
        j = -1
        row_len = int(len(nums) ** (1 / 2))
        for i in range(len(nums)):
            if i % row_len == 0:
                self.rows.append([int(nums[i])])
                j += 1
            else:
                self.rows[j].append(int(nums[i]))

    def add_row(self, src_index, dest_index, multiplier):
        for i in range(len(self.rows)):
            self.rows[dest_index][i] += multiplier * self.rows[src_index][i]
        self.vector[dest_index] += multiplier * self.vector[src_index]

    def solve_matrix(self, vector):
        """takes a square matrix and solves the system of equations"""
        self.vector = vector
        if len(self.rows) != len(self.rows[0]) or len(self.rows) != len(vector):
            return None
        for i in range(len(self.rows)):
            for j in range(len(self.rows)):
                if i == j:
                    divisor = self.rows[i][j]
                    for x in range(len(self.rows)):
                        self.rows[i][x] = self.rows[i][x] / divisor
                    vector[i] = vector[i] / divisor
            # if i + 1 < len(self.rows):
                # find the next 0 there
            for x in range(i + 1, len(self.rows)):
                multiplier = -1 * self.rows[x][i]
                self.add_row(i, x, multiplier)
        print(self.rows)
        print(self.vector)


if __name__ == "__main__":
    a = matrix('2 4 6 1 3 9 1 0 1')
    a.solve_matrix([10, 10, 10])
