import bisect

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

def solve(n, cards, m, nums):

    cards.sort()
    answer = []
    for i in range(m):
        a = bisect.bisect_left(cards, nums[i])
        b = bisect.bisect_right(cards, nums[i])
        print(b, a)
        answer.append(str(b-a))

    print(' '.join(answer))


solve(n, cards, m, nums)

