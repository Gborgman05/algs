from node import Node


def dfs(source):
    discovered = [source]
    paths = []
    print(source.name)
    for adjacent in source.adj:
        paths.append(dfs(adjacent))
    for path in paths:
        for vertex in path:
            discovered.append(vertex)
    return discovered


if __name__ == "__main__":
    root = Node("A")
    second = Node("B")
    third = Node("D")
    fourth = Node("C", weight_list=[1], adjacency_list=root)
    root.add_edge(second)
    second.add_edge(third)
    root.add_edge(fourth)
    dfs(root)
