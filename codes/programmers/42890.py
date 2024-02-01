import itertools


def solution(relations):
    answer = []

    def is_unique(a, rs):
        s = set()
        for r in rs:
            temp = []
            for aa in a:
                temp.append(r[aa])
            s.add('_'.join(temp))

        if len(s) < len(relations):
            return False
        return True

    rlen = len(relations[0])
    a = [i for i in range(rlen)]

    answer_sets = set()

    for i in range(1, rlen+1):
        for c in itertools.combinations(a, i):

            found = False
            for answer_set in answer_sets:
                if set(answer_set).issubset(set(c)):
                    found = True
                    break

            if not found and is_unique(c, relations):
                answer_sets.add(c)
                answer.append(c)

    return len(answer)


if __name__ == '__main__':

    r = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]

    r = solution(r)
    print(r)
    if r == 2:
        print('ok')