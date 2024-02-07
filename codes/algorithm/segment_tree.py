# Segment Tree 구현체

class SegmentTree:

    def __init__(self, data):
        self.data = data
        self.tree = [0] * (len(data)*4)
        return

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            return self.tree[node]
        mid = start + (end - start) // 2
        self.tree[node] = self.init(node*2+1, start, mid) + self.init(node*2+2, mid+1, end)
        return self.tree[node]

    def sum(self, start, end, node, left, right):

        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return self.sum(start, mid, node*2+1, left, right) + self.sum(mid+1, end, node*2+2, left, right)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    tree = SegmentTree(nums)
    tree.init(0, 0, len(nums)-1)
    print('SUM 1 TO 6 : ', tree.sum(0, len(nums)-1, 0, 0, 5))
    print('SUM 1 TO 10 : ', tree.sum(0, len(nums) - 1, 0, 0, 9))
