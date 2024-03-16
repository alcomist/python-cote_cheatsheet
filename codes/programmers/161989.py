def solution(n, m, section):
    answer = 0

    ns = [1] * n
    for s in section:
        ns[s-1] = 0

    for i in range(0, n):

        if ns[i] == 0:
            for j in range(i, i+m):
                if j < n:
                    ns[j] = 1
            answer += 1

    return answer


if __name__ == '__main__':
    
    n = 8
    m = 4
    cs = [2, 3, 6]

    r = solution(n, m, cs)
    if r == 2:
        print('ok')