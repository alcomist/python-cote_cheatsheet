from collections import Counter

def solution(total, tangerine):
    answer = 0

    c = Counter(tangerine)
    for mc in c.most_common():
        if total > 0:
            total -= mc[1]
            answer += 1

    #print(c)
    return answer


if __name__ == '__main__':
    k = 6
    ts = [1, 3, 2, 5, 4, 5, 2, 3]
    r = solution(k, ts)
    if r == 3:
        print('ok')

    k = 4
    ts = [1, 3, 2, 5, 4, 5, 2, 3]
    r = solution(k, ts)
    if r == 2:
        print('ok')

    k = 2
    ts = [1, 1, 1, 1, 2, 2, 2, 3]
    r = solution(k, ts)
    if r == 1:
        print('ok')

