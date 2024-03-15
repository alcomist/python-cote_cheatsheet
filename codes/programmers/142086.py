def solution(s):
    answer = []

    dic = {}

    for i, c in enumerate(s):
        if c not in dic:
            dic[c] = [-1, i]
            answer.append(-1)
        else:
            prev = dic[c]
            dic[c] = [i-prev[1], i]
            answer.append(i-prev[1])

    return answer


if __name__ == '__main__':
    s = "banana"
    r = solution(s)
    if r == [-1, -1, -1, 2, 2, 2]:
        print('ok')