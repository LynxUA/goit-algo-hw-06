import graph

def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = dfs(graph, node, goal, path)
            if new_path:
                return new_path
    return None

def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in set(graph[vertex]) - set(path):
            if next_node == goal:
                return path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))
    return None

G = graph.G
start_capital = "Vienna"
goal_capital = "Madrid"

dfs_path = dfs(G, start_capital, goal_capital)
bfs_path = bfs(G, start_capital, goal_capital)

print(f"DFS path from {start_capital} to {goal_capital}: {dfs_path}")
print(f"BFS path from {start_capital} to {goal_capital}: {bfs_path}")