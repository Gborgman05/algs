# Galen Borgman
# 8/17/2022
# queue

class Q:
    def __init__(self, contents=None):
        if contents:
            self.contents = contents
            self.len = len(contents)
        else:
            self.contents = []
            self.len = 0
    def __len__(self):
        return self.len
    # def enqueue(self, item):

