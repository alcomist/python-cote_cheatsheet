# 파이썬 코딩테스트 Cheat sheet

[트라이 자료 구조](TRIE.md)

## 에라토스테네스의 체
호출시 인자 n까지의 각 숫자의 소수 여부가 True, False로 담겨있음
알고리즘은
1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다.
2. 2는 소수이므로 오른쪽에 2를 쓴다.
3. 자기 자신을 제외한 2의 배수를 모두 지운다.
4. 남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다.
5. 자기 자신을 제외한 3의 배수를 모두 지운다.
6. 남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다.
7. 자기 자신을 제외한 5의 배수를 모두 지운다.
8. 남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다.
9. 자기 자신을 제외한 7의 배수를 모두 지운다.
10. 위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.

최적화는 2부터 해당하는 수의 root의 값까지만 해도 된다.

=> int(math.ceil(n**0.5))+1)  

```python
def build_primes(n):

    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False

    for i in range(2, int(math.ceil(n**0.5))+1):
        if primes[i]:
            for j in range(i*2, n+1, i):
                primes[j] = False

    return primes
```

## 자료구조

## Sort
### Merge sort

### Quick sort

## Tree
Acyclic graph (비순환 그래프)

### Traversal
나무 구조는 나무의 모양을 마치 거꾸로 뒤집어 놓은 모양
뿌라기 가장 위에 있으며 가지들은 밑으로 벌어지며 향함
그리고 잎이 달려있음.

노드 = 버텍스 = 정보가 담겨있는 곳
링크 = 에지 = 노드간의 연결

#### Preorder
1. root를 방문
2. 왼쪽을 방문
3. 오른쪽을 방문
```python
def preorder(node):
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
def inorder(node):
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
def postorder(node):
    if node is None:
        return
        
    postorder(node.left)
    postorder(node.right)
    visit(node.root)
```

#### Levelorder
층별 순회는 Graph의 BFS와 매우 흡사
단 자식에서 뿌리로 올라가는 경로가 Tree구조에서는 유일하므로
discovered 혹은 visited 같은 방문한 곳에 대한 정보가 필요없음

1. 큐에 root를 put
2. 큐가 비어있지 않으면
   3. 큐에서 get하여 방문
   4. 왼쪽 자식이 있으면 put
   5. 오른쪽 자식이 있으면 put
   
```python
def levelorder(node):
    q = [node]
    while q:
        node = pop(0)
        visit(node)
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)
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

전화기 다이얼 패드 영문 조합 코드
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