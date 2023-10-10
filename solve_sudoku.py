class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[] for i in range(len(board))]
        columns = [[] for i in range(len(board))]
        boxes = [[] for i in range(len(board))]
        def get_box(x, y):
            return 3 * (x // 3) + y // 3
        # populate the rows and columns
        insert_count = 0
        for x in range(len(board)):
            for y in range(len(board[x])):
                val = board[x][y]
                if val != ".":
                    rows[x].append(val)
                    columns[y].append(val)
                    boxes[get_box(x, y)].append(val)
                else:
                    insert_count += 1
        # def check_complete():
        #     for i in range(len(board)):
        #         for j in range(len(board)):
        #             val = board[x][y]
        #             if val == ".":
        #                 return False:
        #     return True
        def get_possibilities(x, y):
            possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for num in rows[x]:
                if num in possibilities:
                    possibilities.remove(num)
            for num in columns[x]:
                if num in possibilities:
                    possibilities.remove(num)
            for num in boxes[get_box(x, y)]:
                if num in possibilities:
                    possibilities.remove(num)
            return possibilities
                
            
        while insert_count > 0:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    poss = get_possibilities(i, j)
                    if len(poss) == 1:
                        board[i][j] = poss[0]
                        rows[i].append(poss[0])
                        columns[j].append(poss[0])
                        boxes[get_box(i, j)].append(poss[0])
                        insert_count -= 1
            