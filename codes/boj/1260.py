# 1260. DFS와 BFS

from collections import defaultdict

n, m, v = map(int, input().split())

graph = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


# print(graph)

def dfs(g, start):
    discovered = []
    s = [start]
    while s:
        current = s.pop()
        if current not in discovered:
            discovered.append(current)
            for w in sorted(g[current]):
                s.append(w)
    return discovered


def bfs(g, start):
    visited = [start]
    q = [start]

    while q:

        current = q.pop(0)
        for node in g[current]:
            if node not in visited:
                visited.append(node)
                q.append(node)

    return visited


v1 = dfs(graph, v)
print(' '.join(map(str, v1)))

v2 = bfs(graph, v)
print(' '.join(map(str, v2)))
