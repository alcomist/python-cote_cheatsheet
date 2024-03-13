from itertools import permutations


def solution(n, k):
    answer = []

    perm = permutations(list(range(1, n + 1)))

    for i, p in enumerate(perm):
        if i+1 == k:
            answer = list(p[:])
            break

    return answer


if __name__ == '__main__':

    n = 3
    k = 5
    r = solution(n, k)
    if r == [3, 1, 2]:
        print('ok')
