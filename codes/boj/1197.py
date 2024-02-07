class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a < b:
            self.parent[b] = a
        else:
            self.parent[a] = b

    def has_same_parent(self, a, b):
        a = self.find(a)
        b = self.find(b)

        return True if a == b else False


# 1197. 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197
# cmd : python 1197.py < 1197.txt
# 예제 정답 : 3

def solution():
    v, e = map(int, input().split())

    d = {}

    uf = UnionFind(v)

    for i in range(e):
        a, b, c = map(int, input().split())

        d[(a, b)] = c

    # value로 오름차순으로 정렬
    sorted_d = sorted(d.items(), key=lambda x: x[1])

    answer = 0
    for v in sorted_d:
        a, b = v[0]
        c = v[1]

        # 만약 같은 부모를 가지고 있지 않다면
        if not uf.has_same_parent(a, b):

            # 합쳐주고
            uf.union(a, b)

            # weight를 answer에 더해줌
            answer += c

    return answer


print(solution())

