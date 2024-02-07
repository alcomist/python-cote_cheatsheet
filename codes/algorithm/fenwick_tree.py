class FenwickTree:
    def __init__(self):
        self.n = 0
        self.data = None
        self.tree = None

    def init(self, data):

        self.n = len(data)
        self.data = [0] * (self.n + 1)
        self.tree = [0] * (self.n + 1)

        for i in range(1, len(nums) + 1):
            tree.update(i, data[i - 1])

    def update(self, node, val):

        # node is 0, then return
        if not node:
            return

        diff = val - self.data[node]
        self.data[node] = val
        while node <= self.n:
            self.tree[node] += diff
            node += (node & -node)

    def sum(self, node):
        res = 0
        while node > 0:
            res += self.tree[node]
            node -= (node & -node)
        return res


if __name__ == '__main__':

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree = FenwickTree()
    tree.init(nums)

    print(tree.sum(10))

    tree.update(0, 10)
    tree.update(1, 10)

    print(tree.sum(10))
