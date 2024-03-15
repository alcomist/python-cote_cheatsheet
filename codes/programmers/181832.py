def solution(n):
    answer = [[0] * n for _ in range(n)]
    print(answer)

    

    return answer


if __name__ == '__main__':
    n = 4
    r = solution(n)
    if r == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]:
        print('ok')
