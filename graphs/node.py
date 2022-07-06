import sys


class Node:
    def __init__(self, name=None, adjacency_list=[], weight_list=[] ):
        self.adj = adjacency_list
        self.weights = weight_list
        self.name = name

    def add_edge(self, node, weight=1):
        self.adj.append(node)
        self.weights.append(weight)

    def shortest_out(self):
        min_weight = sys.maxsize
        min_index = 0
        for i in range(len(self.weights)):
            if min_weight > self.weights[i]:
                min_weight = self.weights[i]
                min_index = i
        return [min_index, min_weight]
