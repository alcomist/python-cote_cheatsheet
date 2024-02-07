class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n+1))

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


if __name__ == '__main__':

    n = 10

    union = UnionFind(n)
    union.union(0, 1)
    union.union(2, 3)
    union.union(3, 4)

    # True
    print(union.find(0) == union.find(1))

    # False
    print(union.find(1) == union.find(2))

    # True
    print(union.find(2) == union.find(4))

    #true
    print(union.find(3) == union.find(4))

