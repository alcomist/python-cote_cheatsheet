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

