# 파이썬 코딩테스트 Cheat sheet

## 문제 풀이
| 주제                    |
|-----------------------|
| [알고리즘] (ALGORITHM.md) |
| [트리] (TREE.md)        |
| [그래프] (GRAPH.md)      |
| [정렬] (SORT.md)        |

## 자료구조





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