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


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree = [0] * (len(nums) * 4)

    init_segment_tree(nums, 0, 0, len(nums)-1)
    print('SUM 1 TO 6 : ', tree_sum(0, len(nums)-1, 0, 0, 5))
