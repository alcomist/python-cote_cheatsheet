
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

def solve(n, m, a):

    start = 0
    end = a[-1]

    while start+1 < end:

        mid = (start + end) // 2

        logs = 0
        for i in range(n):
            if trees[i] > mid:
                logs += trees[i]-mid

        if logs >= m:
            start = mid
        else:
            end = mid

    return start


print(solve(n, m, trees))
