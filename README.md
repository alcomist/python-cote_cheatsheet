# 파이썬 코딩테스트 Cheat sheet

## 자료구조

## Sort
### Merge sort

### Quick sort

## Tree
Acyclic graph (비순환 그래프)

### Traversal

#### Preorder
1. root를 방문
2. 왼쪽을 방문
3. 오른쪽을 방문
```python
void preorder(node):
    if node is None:
        return
        
    visit(node.root)
    preorder(node.left)
    preorder(node.right)
```

#### Inorder
1. 왼쪽을 방문
2. root를 방문
3. 오른쪽을 방문
```python
void inorder(node):
    if node is None:
        return
        
    inorder(node.left)
    visit(node.root)
    inorder(node.right)
```

#### Postorder
1. 왼쪽을 방문
2. 오른쪽을 방문
3. root를 방문
```python
void postorder(node):
    if node is None:
        return
        
    postorder(node.left)
    postorder(node.right)
    visit(node.root)
```

### 트라이
```python
tree = [0] * 2**(ceil(log(n, 2) + 1))
```

## 그래프
### DFS (깊이 우선 탐색)
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

### BFS (너비 우선 탐색)
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

### 모든 조합 탐색

```python
def comb(s):
    
    answer = []
    def dfs(index, path):
        if len(path) == len(s):
            answer.append(paht)
            return
            
        for i in range(index, len(s)):
            for j in dic[s[i]]:
                dfs(i+1, path + j)
    
    if not digits:
        return []
        
    dic = {'2': 'abc', '3': 'def ...}
    dfs(0, '')
    
    return answer
```

```python
def combination(n, k):
    answer = []

    def dfs(a, s, k):
        if k == 0:
            answer.append(a[:])
            return

        for i in range(s, n+1):
            dfs(a + [i], s+1, k-1)

    dfs([], 1, k)
    return answer
```