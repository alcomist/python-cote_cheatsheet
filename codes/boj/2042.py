import math

N, M, K = map(int, input().split())

nums = [0] * N
for i in range(N):
    nums[i] = int(input().strip())

#print(nums)




height = math.ceil(math.log(len(nums), 2))
tree_size = pow(2, height+1) - 1

tree = [0] * tree_size


def init_segment_tree(tree, nodes, index, left, right):
    if left == right:
        tree[index] = nodes[left]
        return tree[index]
    mid = (left + right) // 2
    tree[index] = init_segment_tree(tree, nodes, index*2+1, left, mid) + init_segment_tree(tree, nodes, index*2+2, mid + 1, right)

    return tree[index]


def tree_update(start, end, index, diff):
    if start > index or index > end:
        return tree[index]
    tree[index] += diff
    if start != end:
        mid = (start + end) // 2
        tree_update(start, mid, index * 2 + 1, diff)
        tree_update(mid + 1, end, index * 2 + 2, diff)



def tree_sum(start, end, i, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[i]
    mid = (start + end) // 2
    return tree_sum(start, mid, i*2+1, left, right) + tree_sum(mid+1, end, i*2+2, left, right)


init_segment_tree(tree, nums, 0, 0, len(nums)-1)

for i in range(M+K):
    a, b, c = map(int, input().strip().split())
    if a == 1:
        tree_update(0, len(nums)-1, b-1, c-nums[b-1])
    else:
        print(tree_sum(0, len(nums)-1, 0, b-1, c-1))
