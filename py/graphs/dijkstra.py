import sys


def main():
    pass
class node():
    def __init__(self, adjacency_list, weight_list):
        self.adj = adjacency_list
        self.weights = weight_list
    def shortest_out(self):
        min_weight = sys.maxsize
        min_index = 0
        for i in range(len(self.weights)):
            if min_weight > self.weights[i]:
                min_weight = self.weights[i]
                min_index = i
        return [min_index, min_weight]
class Graph():
    # graph definition from https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[[0 for column in range(vertices)]
                      for row in range(vertices)]]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])
def dijkstra(graph, src):
    path_len = [sys.maxsize] * len(graph.vertices)
    path_len[src] = 0
    spt_set = [False] * len(graph.vertices)




if __name__ == "__main__":
    main()