import bisect
import collections
import itertools


def solution_old(infos, queries):
    answer = []

    info_dic = collections.defaultdict(set)

    scores = [0] * len(infos)

    for user_index, info in enumerate(infos):
        a, b, c, d, e = info.split()
        info_dic[a].add(user_index)
        info_dic[b].add(user_index)
        info_dic[c].add(user_index)
        info_dic[d].add(user_index)
        scores[user_index] = int(e)

    for query in queries:
        a, b, c, d = query.split(' and ')
        d, e = d.split()
        score = int(e)

        temp = set([user_index for user_index, user_score in enumerate(scores) if user_score >= score])
        for i in [a, b, c, d]:
            if i in info_dic:
                temp = temp.intersection(info_dic[i])

        answer.append(len(temp))

    return answer


def solution_slow1(infos, queries):
    answer = []

    info_dic = collections.defaultdict(set)

    scores = [0] * len(infos)

    for user_index, info in enumerate(infos):
        a, b, c, d, e = info.split()
        info_dic[a].add(user_index)
        info_dic[b].add(user_index)
        info_dic[c].add(user_index)
        info_dic[d].add(user_index)
        scores[user_index] = int(e)

    for query in queries:
        a, b, c, d = query.split(' and ')
        d, e = d.split()
        score = int(e)

        temp = []
        temp.extend([user_index for user_index, user_score in enumerate(scores) if user_score >= score])
        cond_count = 1

        for i in [a, b, c, d]:
            if i in info_dic:
                cond_count += 1
                temp.extend(info_dic[i])

        counter = collections.Counter(temp)
        #print(counter)
        answer.append(len([k for k, v in counter.items() if v == cond_count]))
        #answer.append(len(temp))

    return answer


def solution(infos, queries):
    answer = []

    binaries = list(itertools.product((True, False), repeat=4))
    info_dic = collections.defaultdict(list)

    for info in infos:
        info = info.split()

        for binary in binaries:
            key = ''.join([info[i] if binary[i] else '-' for i in range(4)])
            info_dic[key].append(int(info[4]))

    for k in info_dic.keys():
        info_dic[k].sort()


    for query in queries:
        a, b, c, d = query.split(' and ')
        d, e = d.split()
        score = int(e)

        key = ''.join([a, b, c, d])
        i = bisect.bisect_left(info_dic[key], score)
        answer.append(len(info_dic[key])-i)

    return answer


if __name__ == '__main__':

    info = ["java backend junior pizza 150",
             "python frontend senior chicken 210",
             "python frontend senior chicken 150",
             "cpp backend senior pizza 260",
             "java backend junior chicken 80",
             "python backend senior chicken 50"]

    query = ["java and backend and junior and pizza 100",
               "python and frontend and senior and chicken 200",
               "cpp and - and senior and pizza 250",
               "- and backend and senior and - 150",
               "- and - and - and chicken 100",
               "- and - and - and - 150"]

    r = solution(info, query)
    if r == [1, 1, 1, 1, 2, 4]:
        print('ok')
