import collections
import itertools


def solution(friends, gifts):
    answer = 0

    gift_index = collections.defaultdict(int)
    gift_dic = collections.defaultdict(dict)

    for a, b in itertools.combinations(friends, 2):
        if a not in gift_dic:
            gift_dic[a] = collections.defaultdict(int)
            gift_dic[a][b] = 0
        if b not in gift_dic:
            gift_dic[b] = collections.defaultdict(int)
            gift_dic[b][a] = 0

    for gift in gifts:
        a, b = gift.split()
        gift_index[a.strip()] += 1
        gift_index[b.strip()] -= 1
        gift_dic[a][b] += 1

    gift_count = collections.defaultdict(int)

    for a, b in itertools.combinations(friends, 2):
        # 내가 준적이 있다
        if gift_dic[a][b] == gift_dic[b][a]:
            if gift_index[a] > gift_index[b]:
                gift_count[a] += 1
            elif gift_index[a] < gift_index[b]:
                gift_count[b] += 1
        else:
            if gift_dic[a][b] > gift_dic[b][a]:
                gift_count[a] += 1
            elif gift_dic[a][b] < gift_dic[b][a]:
                gift_count[b] += 1

    if len(gift_count) == 0:
        return 0
    return max(gift_count.values())


if __name__ == '__main__':

    f = ["muzi", "ryan", "frodo", "neo"]
    g = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

    r = solution(f, g)
    print(r)
    if 2 == r:
        print('ok')

    f = ["joy", "brad", "alessandro", "conan", "david"]
    g = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

    r = solution(f, g)
    print(r)
    if 4 == r:
        print('ok')

    f = ["a", "b", "c"]
    g = ["a b", "b a", "c a", "a c", "a c", "c a"]
    r = solution(f, g)
    print(r)
    if 0 == r:
        print('ok')
