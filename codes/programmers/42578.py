import collections
import itertools
import math

def solution(clothes):
    answer = 1

    part_dic = collections.defaultdict(list)

    for c in clothes:
        part_dic[c[1]].append(c[0])

    for k, v in part_dic.items():
        answer *= (len(v)+1)

    return answer-1


if __name__ == '__main__':

    c = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    r = solution(c)
    print(r)
    if r == 5:
        print('ok')

    c = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    r = solution(c)
    print(r)
    if r == 3:
        print('ok')

