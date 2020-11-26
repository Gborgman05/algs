class Matrix:

    def __init__(self, nums, name="Unnamed"):
        self.rows = []
        self.vector = []
        self.name = name
        nums = nums.split(' ')
        j = -1
        row_len = int(len(nums) ** (1 / 2))
        for i in range(len(nums)):
            if i % row_len == 0:
                self.rows.append([int(nums[i])])
                j += 1
            else:
                self.rows[j].append(int(nums[i]))

    def verify_square(self):
        try:
            for row in self.rows:
                a = row[len(self.rows) - 1]
            return True
        except IndexError:
            return False

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
        self.percolate_up()
        self.display_matrix()
        print(self.vector)

    def percolate_up(self):
        for i in range(len(self.rows) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                multiplier = -1 * self.rows[j][i]
                self.add_row(i, j, multiplier)

    def matrix_multiply(self, multiplier):
        multiplier.verify_square()
        answer_matrix = []
        for i in range(len(self.rows)):
            answer_matrix.append([])
            for j in range(len(multiplier.rows)):
                val = 0
                for x in range(len(self.rows)):
                    val += self.rows[i][x] * multiplier.rows[x][j]
                answer_matrix[i].append(val)
        answer = self.build_matrix(answer_matrix)
        answer.display_matrix()
        # go across the row and get the column values

    def build_matrix(self, matrix):
        string = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                string += "{} ".format(matrix[i][j])
        return Matrix(string.rstrip())

    def display_matrix(self):
        lines = [self.name, " " + "_" * (len(self.rows) * 2 - 1)]
        for i in range(len(self.rows)):
            line = "|"
            for j in range(len(self.rows[i])):
                line += (str(self.rows[i][j]) + "|")
            lines.append(line)
        for line in lines:
            print(line)


if __name__ == "__main__":
    a = Matrix('2 4 6 1 3 9 1 0 1')
    a.display_matrix()
    a.solve_matrix([10, 10, 10])
    b = Matrix('1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1')
    b.display_matrix()
    b.solve_matrix([1, 1, 1, 1])
