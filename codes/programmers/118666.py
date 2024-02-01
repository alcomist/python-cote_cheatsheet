import collections


def solution(survey, choices):

    answer = []

    d = collections.defaultdict(int)

    for i, choice in enumerate(choices):
        if choice < 4:
            d[survey[i][0]] += 4 - choice
        elif choice > 4:
            d[survey[i][1]] += choice - 4

    for p in [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]:
        a = d[p[0]]
        b = d[p[1]]
        if a > b:
            answer.append(p[0])
        elif a < b:
            answer.append(p[1])
        else:
            answer.append(p[0] if ord(p[0]) < ord(p[1]) else p[1])

    return ''.join(answer)



if __name__ == '__main__':
    s = ["AN", "CF", "MJ", "RT", "NA"]
    #c = [5, 3, 2, 7, 5]
    c = [4, 4, 4, 4, 4]

    r = solution(s, c)
    print(r)
    if r == "TCMA":
        print('ok')

    s = ["TR", "RT", "TR"]
    c = [7, 1, 3]
    r = solution(s, c)
    if r == "RCJA":
        print('ok')