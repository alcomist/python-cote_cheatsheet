# Tree
Acyclic graph (비순환 그래프)

## Traversal
나무 구조는 나무의 모양을 마치 거꾸로 뒤집어 놓은 모양
뿌라기 가장 위에 있으며 가지들은 밑으로 벌어지며 향함
그리고 잎이 달려있음.

노드 = 버텍스 = 정보가 담겨있는 곳

링크 = 에지 = 노드간의 연결

### Preorder
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

### Inorder
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

### Postorder
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

### Levelorder
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

### 트라이
```python
tree = [0] * 2**(ceil(log(n, 2) + 1))
```