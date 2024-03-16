def solution(sequence, k):
    n = len(sequence)

    result = 0
    end = 0
    interval = n

    answer = []

    for start in range(n):
        while result < k and end < n:
            result += sequence[end]
            end += 1
        if result == k and end-1-start < interval:
            answer = [start, end-1]
            interval = end-1-start
        result -= sequence[start]

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
