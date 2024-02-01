import collections
import math

def solution(name):

    answer = []

    start = collections.deque(['A'] * len(name))
    end = collections.deque(list(name))

    visit = {}

    def solve(s, e, m):


    solve(start, end, 0)
    #print(answer)
    return max(answer)-1


if __name__ == '__main__':

    n = "JAZ"
    r = solution(n)
    print(r)
    if r == 11:
        print('ok')

    n = "JEROEN"
    r = solution(n)
    print(r)
    if r == 56:
        print('ok')

    n = "JAN"
    r = solution(n)
    print(r)
    if r == 23:
        print('ok')

