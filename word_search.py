class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        new_word = []
        for i in range(len(word) - 1, -1, -1):
            new_word.append(word[i])

        def helper(remaining, used, x, y):
            #print(remaining)
            if not remaining:
                #print(x, y, used)
                return True
            if x < 0 or x >= len(board[0]):
                return False
            if y < 0 or y >= len(board):
                return False
            if (x, y) in used:
                return False
            if board[y][x] == remaining[-1]:
                #used.append((x, y))
                #print(used)
                return helper(remaining[:-1], used + [(x, y)], x+1, y) or helper(remaining[:-1], used + [(x, y)], x, y + 1) or helper(remaining[:-1], used + [(x, y)], x-1, y) or helper(remaining[:-1], used + [(x, y)], x, y-1)
            else:
                return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(new_word, [], j, i):
                    return True
        return False
