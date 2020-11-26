# Created by gbrgm on 11/25/2020
# Title: Source Removal Algorithm

class Node:
    def __init__(self, name=None, adjacent=[]):
        self.name = name
        self.adjacent = adjacent
class Graph:
    def __init__(self):
        self.nodes = []
    def add_node(self, node):
        self.nodes.append(node)

def source_removal(graph):
    in_degree = {
    }
    for node in graph:
        if node not in in_degree:
            in_degree[node] = 0
        for adjacent in graph[node]:
            if adjacent not in in_degree:
                in_degree[adjacent] = 1
            else:
                in_degree[adjacent] += 1
    # print(in_degree)
    dependency_resolution = []
    while len(in_degree.keys()) > 0:
        for key, value in in_degree.items():
            if value == 0:
                dependency_resolution.append(key)
                for adjacent in graph[key]:
                    in_degree[adjacent] -= 1
                del in_degree[key]
                break
    return dependency_resolution

if __name__ == "__main__":
    # graph = Graph()
    # graph.add_node(Node("D"))
    # graph.add_node(Node("B", [graph.nodes[0]]))
    # graph.add_node(Node("E", [graph.nodes[0]]))
    graph = {
        "G": ["A", "F"],
        "A": ["B", "C"],
        "C": ["E", "F"],
        "F": ["E"],
        "E": ["D"],
        "B": ["D"],
        "D": []
    }
    print(source_removal(graph))


