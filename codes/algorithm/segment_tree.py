# Segment Tree 구현체
import math


class SegmentTree:

    def __init__(self):

        self.tree = None
        self.data = None
        return

    def _init(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            return self.tree[node]
        mid = start + (end - start) // 2
        self.tree[node] = self._init(node * 2 + 1, start, mid) + self._init(node * 2 + 2, mid + 1, end)
        return self.tree[node]

    def init(self, data):
        self.data = data

        # 1. 트리의 높이 h는 log2( leaf 노드의 수(원래 data 배열의 원소 수) )를 올림하여 구할 수 있다.
        # 2. 등비수열의 합 공식에 의해, 2^(h+1)이 된다.

        node_count = (1 << math.ceil(math.log2(len(data))) + 1)

        self.tree = [0] * node_count
        self._init(0, 0, len(data) - 1)

    def _sum(self, start, end, node, left, right):

        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = start + (end - start) // 2
        return self._sum(start, mid, node * 2 + 1, left, right) + self._sum(mid + 1, end, node * 2 + 2, left, right)

    def sum(self, node, left, right):
        return self._sum(0, len(self.data) - 1, node, left, right)

    def update(self, pos, val):
        if pos >= len(self.data):
            return

        self.data[pos] = val

        self._update(0, len(self.data) - 1, 0, pos, val)


    def _update(self, start, end, node, pos, val):

        # position이 start, end를 벗어나면 리턴
        if pos > end or pos < start:
            return self.tree[node]

        # pos 가 start 와 end 구간 안에 있다면 업데이트
        if start == end:
            self.tree[node] = val
            return self.tree[node]

        # 분할 재귀
        mid = start + (end - start) // 2
        self.tree[node] = self._update(start, mid, node * 2 + 1, pos, val) + self._update(mid+1, end, node * 2 + 2, pos, val)
        return self.tree[node]

    def _update_diff(self, start, end, node, pos, diff):

        if pos < start or end < pos:
            return

        self.tree[node] += diff

        if start == end:
            return

        mid = start + (end - start) // 2
        self._update_diff(start, mid, node * 2 + 1, pos, diff)
        self._update_diff(mid + 1, end, node * 2 + 2, pos, diff)

    # diff 값만 업데이트
    def update_diff(self, pos, value):

        diff = value - self.data[pos]
        self.data[pos] = value

        self._update_diff(0, len(self.data)-1, 0, pos, diff)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    tree = SegmentTree()
    tree.init(nums)
    print('SUM 1 TO 6 : ', tree.sum(0, 0, 5))
    print('SUM 1 TO 10 : ', tree.sum(0, 0, 9))

    #tree.update(9, 12)
    tree.update_diff(9, 12)
    print('SUM 1 TO 10 : ', tree.sum(0, 0, 9))

    #tree.update(9, 10)
    tree.update_diff(9, 10)
    print('SUM 1 TO 10 : ', tree.sum(0, 0, 9))

    #tree.update(0, 10)
    tree.update_diff(0, 10)
    print('SUM 1 TO 10 : ', tree.sum(0, 0, 9))
