# 파이썬 코딩테스트 Cheat sheet
---

직접 input 받을 때
- 일반적으로 list, map 을 활용

```python
# 공백을 기준으로 구분된 데이터를 입력 받을 떄
data = list(map(int, input().split()))
```

```python
# 공백을 기준으로 구분된 데이터가 많지 않다면
a, b, c = map(int, input().split())
```

- sys stdin을 활용해 빠른 input 받기 (꼭 직접 입력을 받아야 한다면, 추천)

import sys

```python
# 공백으로 구분된 2개 숫자 입력 받기
N, M = map(int,sys.stdin.readline().split())

# 2차원 리스트 입력 받기
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
```

--- 

## 수학

Modulo 연산

나머지 연산(%)도 나눗셈을 제외하면 분배법칙이 적용된다.

```
(A + B) % N = ((A % N) + (B % N)) % N
```
다음의 법칙이 성립한다는 것인데 이를 증명해보면 다음과 같다.

A 와 B에 해당하는 몫과 나머지를 각각 [q1 r1], [q2 r2] 로 가정해보자.
그러면

```
A = q1 X N + r1
B = q2 X N + r2
```
A, B를 나타낼 수 있고 이를 오른쪽 항에 대입하면

```
(q1 X N + r1 + q2 X N + r2) % N
= ((q1+q2) X N + r1 + r2) % N
```

로 치환할 수 있다. 그러면 결국 modulo 는 나머지 연산이기 때문에
몫에 해당하는 q1 와 q2 는 결국 나머지 연산 과정에서 0 이 되어
남는 것은

```
(r1 + r2) % N
```

이다. 이때 r1 과 r2 는 위에서 나타낸 대로 대한 A와 B의 나머지이므로
이는 결국

```
r1 = A % N
r2 = B % N
```

이 된다. 따라서

```
(A + B) % N = ((A % N) + (B % N)) % N
```

이 성립한다는 것을 증명할 수 있다.

--- 
## 알고리즘

### 쿼드트리 뒤집기

[쿼드트리 테스트 코드](python/quadtree.py)

buffer를 생성시에 아래와 같이 생성하면

참조 값이 들어가서 제대로 된 업데이트를 할 수 없다.
```python
row = ['1'] * 100
decompressed = [row] * 100
```

아래와 같이 buffer를 생성해야 정상적으로 처리할 수 있다.

```python
cols = rows = 100
decompressed = [['' for j in range(cols)] for i in range(rows)]

def decompress(str, y, x, size):

    head = str[0]
    temp = str[1:]
    if head == 'b' or head == 'w':
        for dy in range(size):
            for dx in range(size):
                decompressed[y+dy][x+dx] = head
    else:
        half = size//2
        temp = decompress(temp, y, x, half)
        temp = decompress(temp, y, x+half, half)
        temp = decompress(temp, y+half, x, half)
        temp = decompress(temp, y+half, x+half, half)

    return temp
```

### 카데인 알고리즘

```python
def max_subsum(nums):
    answer = -999999
    psum = 0
    for num in nums:
        psum = max(psum, 0) + num
        answer = max(psum, answer)
    
    return answer
```

### 하노이의 탑

고전 컴퓨터 알고리즘 인 파이썬 코드
```python
def hanoi(start, transit, end, n):
    if n <= 0:
        return
    
    hanoi(start, end, transit, n-1)
    print(f"{n}번째 원반을 '{start}' 에서 '{transit}'으로 이동")
    hanoi(end, transit, start, n-1)
```

C로 배우는 알고리즘 코드
```python
def hanoi(n, start, transit, end):
    if n == 1:
        print(f"{n}번째 원반을 '{start}' 에서 '{end}'으로 이동")
    else:
        hanoi(n-1, start, end, transit)
        print(f"{n}번째 원반을 '{start}' 에서 '{end}'으로 이동")
        hanoi(n-1, transit, start, end)
```

### 에라토스테네스의 체

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

최적화는 2부터 해당하는 수의 root의 값까지만 체크해도 됨.

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
--- 
## Tree
Acyclic graph (비순환 그래프)

### Traversal
나무 구조는 나무의 모양을 마치 거꾸로 뒤집어 놓은 모양
뿌리가 가장 위에 있으며 가지들은 밑으로 벌어지며 향함
그리고 잎이 달려있음.

노드 = 버텍스 = 정보가 담겨있는 곳

링크 = 에지 = 노드간의 연결

#### Preorder
1. 뿌리를 방문
2. 왼쪽 작은 나무를 방문
3. 오른쪽 작은 나무를 방문
```python
def preorder(node):
    if node is None:
        return
        
    visit(node.root)
    preorder(node.left)
    preorder(node.right)
```

#### Inorder
1. 왼쪽 작은 나무를 방문
2. 뿌리를 방문
3. 오른쪽 작은 나무를 방문
```python
def inorder(node):
    if node is None:
        return
        
    inorder(node.left)
    visit(node.root)
    inorder(node.right)
```

#### Postorder
1. 왼쪽 작은 나무를 방문
2. 오른쪽 작은 나무를 방문
3. 뿌리를 방문
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
    1) 큐에서 get하여 방문
    2) 방문한 node 왼쪽 자식이 있으면 put
    3) 방문한 node 오른쪽 자식이 있으면 put

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

### 세그먼트 트리 (Segmemnt tree)

구간 트리 

세그먼트 트리를 이용하면, 1번 연산을 O(logN), 2번 연산도 O(logN)만에 수행 가능

세그먼트 트리의 리프 노드와 리프 노드가 아닌 다른 노드는 다음과 같은 의미를 가진다.

1) 리프 노드 : 배열의 그 수 자체

2) 다른 노드 : 왼쪽 자식과 오른쪽 자식의 합을 저장함.

1. 루트가 0으로 시작하는 경우
- 노드의 번호가 i일때, 왼쪽 자식의 번호는 2*i+1, 오른쪽 자식의 번호는 2*i + 2가 된다.
2. 루트가 1로 시작하는 경우
- 노드의 번호가 i일때, 왼쪽 자식의 번호는 2*i, 오른쪽 자식의 번호는 2*i + 1이 된다.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = [0] * (len(nums)*4)

def init_segment_tree(a, i, left, right):
    if left == right:
        tree[i] = a[left]
        return tree[i]
    mid = (right+left)//2
    tree[i] = init_segment_tree(a, i*2+1, left, mid) + init_segment_tree(a, i*2+2, mid+1, right)
    return tree[i]


def tree_sum(start, end, i, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[i]
    mid = (start + end) // 2
    return tree_sum(start, mid, i*2+1, left, right) + tree_sum(mid+1, end, i*2+2, left, right)


init_segment_tree(nums, 0, 0, len(nums)-1)

print('sum 0 to 5 : ', tree_sum(0, len(nums)-1, 0, 0, 5))
```


### 펜윅트리 (Fenwick tree)
바이너리 인덱스 트리라고도 불림
세그먼트 트리와 비슷하나 구간합이 아닌 누적합을 가지고 있어 구간합을 구하려면
앞부분의 인덱스를 빼줘야 한다.

```python
class FenwickTree:
   def __init__(self, n):
      self.n = n
      self.arr = [0]*(n+1)
      self.tree = [0]*(n+1)
   
    def update(self, i, num):
        self.arr[i] += num
        while i <= self.n:
            self.tree[i] += num
            i += (i & -i)

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree = FenwickTree(len(nums))
    for i in range(1, len(nums)+1):
        tree.update(i, nums[i-1])

    print(tree.sum(10))
```

### 트라이

트라이(Trie)는 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조

우리가 검색할 때 볼 수 있는 자동완성 기능, 사전 검색 등 문자열을 탐색하는데 특화되어있는 자료구조

래딕스 트리(radix tree) or 접두사 트리(prefix tree) or 탐색 트리(retrieval tree)라고도 함.

트라이는 retrieval tree에서 나온 단어

예를 들어 'Algorithm'라는 단어를 검색하기 위해서는 제일 먼저 'A'를 찾고, 다음에 'l', 'g', ... 의 순서로 찾으면 된다. 이러한 개념을 적용한 것이 트라이(Trie)이다.

```python
class TrieNode(object):
    def __init__(self, key, terminal=False):
        self.key = key
        self.terminal = terminal
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = TrieNode(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode(char)

            curr_node = curr_node.children[char]

        curr_node.terminal = True

    def search(self, string):

        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        return curr_node.terminal

```
--- 
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
--- 
## 모든 조합 탐색

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