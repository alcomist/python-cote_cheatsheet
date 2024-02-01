import collections
import itertools

def solution(orders, courses):

    def solve(orders, course):

        r = []
        d = collections.defaultdict(int)
        for order in orders:
            for c in itertools.combinations(sorted(list(order)), course):
                d[''.join(c)] += 1

        if len(d) == 0:
            return []

        c = collections.Counter(d)
        max_value = max(list(c.values()))

        if max_value == 1:
            return []

        for key in list(c.keys()):
            if c[key] == max_value:
                r.append(key)

        return r


    answer = []
    for c in courses:
        answer.extend(solve(orders, c))

    return sorted(answer)


if __name__ == '__main__':
    o = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    c = [2, 3, 4]

    r = solution(o, c)
    print(r)
    if r == ["AC", "ACDE", "BCFG", "CDE"]:
        print('ok')

    o = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    c = [2, 3, 5]

    r = solution(o, c)
    print(r)
    if r == ["ACD", "AD", "ADE", "CD", "XYZ"]:
        print('ok')

    o = ["XYZ", "XWY", "WXA"]
    c = [2, 3, 4]
    r = solution(o, c)
    print(r)
    if r == ["WX", "XY"]:
        print('ok')