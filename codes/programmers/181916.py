from collections import defaultdict


def solution(a, b, c, d):
    answer = 0

    dic = defaultdict(int)

    dic[a] += 1
    dic[b] += 1
    dic[c] += 1
    dic[d] += 1

    keys = dic.keys()
    key_len = len(keys)
    if key_len == 4:
        answer = min(keys)
    

    return answer


if __name__ == '__main__':

    a = 2
    b = 2
    c = 2
    d = 2
    r = solution(a, b, c, d)
    if r == 2222:
        print('ok')
