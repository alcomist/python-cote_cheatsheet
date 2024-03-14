def solution(n):
    answer = 0

    ls = list(range(1, n+1))
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break

    return answer


if __name__ == '__main__':

    n = 15
    r = solution(n)
    if r == 4:
        print('ok')
