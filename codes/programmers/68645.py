def solution(n):
    answer = [[0 for _ in range(1, i+1)] for i in range(1, n+1)]
    print(answer)
    return answer

if __name__ == '__main__':

    nn = 4
    r = solution(nn)
    if r == [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]:
        print('ok')

    nn = 5
    r = solution(nn)
    if r == [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]:
        print('ok')

    nn = 6
    r = solution(nn)
    if r == [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]:
        print('ok')