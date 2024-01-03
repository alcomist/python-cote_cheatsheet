# 그래프
## DFS (깊이 우선 탐색)
스택으로 구현하며, 재귀를 이용하면 좀더 간단하게 구현 가능

```python
def recur_dfs(v, discovered = []):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recur_dfs(w, discovered)
    return discovered
```

```python
def iter_dfs(v):
    discovered = []
    s = [v]
    while s:
        v = s.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered
```

## BFS (너비 우선 탐색)
큐로 구현하며, 재귀로 풀이 불가능

```python
def bfs(v):
    discovered = []
    q = [v]
    while q:
        v = q.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                q.append(w)
    return discovered
```