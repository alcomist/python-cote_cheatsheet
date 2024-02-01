import bisect
import collections
import itertools


def solution_slow(dice):
    answer = []

    prob = {}

    s = set(range(len(dice)))
    for c in itertools.combinations(s, len(dice)//2):

        a = list(c)
        key = ' '.join(map(str, map(lambda x: x+1, a)))
        print(key)

        win, lose, draw = 0, 0, 0

        prob[key] = 0.0

        b = list(s.difference(c))

        for r in [[sum(list(x)), sum(list(y))] for x in list(itertools.product(*[dice[x] for x in a]))
             for y in list(itertools.product(*[dice[x] for x in b]))]:

            if r[0] > r[1]:
                win += 1
            elif r[0] < r[1]:
                lose += 1
            else:
                draw += 1

        prob[key] = win / (win+lose+draw)

    p = sorted(prob.items(), key=lambda x: x[1], reverse=True)
    return list(map(int, p[0][0].split()))


def solution(dice):

    prob = {}
    dice_sum = collections.defaultdict(list)

    s = set(range(len(dice)))
    for c in itertools.combinations(s, len(dice)//2):

        a = list(c)
        key = ' '.join(map(str, map(lambda x: x+1, a)))

        dice_sum[key] = [sum(x) for x in list(itertools.product(*[dice[x] for x in a]))]
        dice_sum[key].sort()

    for c in itertools.combinations(s, len(dice)//2):
        akey = ' '.join(map(str, map(lambda x: x + 1, list(c))))
        bkey = ' '.join(map(str, map(lambda x: x + 1, s.difference(list(c)))))

        prob[akey] = 0

        win = 0

        for x in dice_sum[akey]:
            win += bisect.bisect_left(dice_sum[bkey], x)

        prob[akey] = win

    p = sorted(prob.items(), key=lambda x: x[1], reverse=True)
    return list(map(int, p[0][0].split()))



if __name__ == '__main__':

    d = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
    r = solution(d)
    print(r)
    if r == [1, 4]:
        print('ok')
    exit()

    d = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
    r = solution(d)
    if r == [2]:
        print('ok')

    d = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
    r = solution(d)
    if r == [1, 3]:
        print('ok')