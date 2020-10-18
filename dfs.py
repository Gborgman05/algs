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
    second.add_edge(Node("D"))
    root.add_edge(second)
    root.add_edge(Node("C"))
    this = root.adj[0]
    (root.adj[0]).add_edge(Node("D"))
    dfs(root)
