n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


def restore(s1, e1, s2, e2):
    if s1 < e1 and s2 < e2:
        root = inorder.index(postorder[e2])
        val = inorder[root]
        print(val, end=' ')

        leftNode = nodeNum[root] - inStart
        rightNode = inEnd - nodeNum[root]

        print(root, end=" ")
        preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
        preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

        left_len = len(inorder[0:index])
        right_len = len(inorder[index+1:])
        restore(s1, index-1, s2, left_len-1)
        restore(s1 + index+1, right_len-1, left_len, left_len+right_len-1)


restore(0, n-1, 0, n-1)