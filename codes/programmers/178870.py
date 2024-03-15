def solution(sequence, k):
    answer = []
    return answer


if __name__ == '__main__':

    ss = [1, 2, 3, 4, 5]
    k = 7
    r = solution(ss, k)
    if r == [2, 3]:
        print('ok')

    ss = [1, 1, 1, 2, 3, 4, 5]
    k = 5
    r = solution(ss, k)
    if r == [6, 6]:
        print('ok')

    ss = [2, 2, 2, 2, 2]
    k = 6
    r = solution(ss, k)
    if r == [0, 2]:
        print('ok')
