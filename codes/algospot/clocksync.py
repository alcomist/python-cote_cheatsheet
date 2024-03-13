# 6.4 문제: 시계 맞추기 (문제 ID: CLOCKSYNC, 난이도: 중)
# 4 x 4 개의 격자 형태로 배치된 열여섯 개의 시계를 스위치를 눌러서
# 모두 12시를 가리키도록 해야 함.

import sys


def solution(clocks):
    switch_count = 10
    clock_count = 16

    if len(clocks) != clock_count:
        print('INVALID INPUT')
        return

    answer = 0

    # 스위치는 16개로 이루어짐  0123456789012345
    linked = ['xxx.............',
              '...x...x.x.x....',
              '....x.....x...xx',
              'x...xxxx........',
              '......xxx.x.x...',
              'x.x...........xx',
              '...x..........xx',
              '....xx.x......xx',
              '.xxxxx..........',
              '...xxx...x...x..']

    def aligned():
        for clock in clocks:
            if clock != 12:
                return False
        return True

    # 해당하는 시계와 스위치가 연결되어 있다면 3시간씩 시침을 오른쪽으로 회전시킨다.
    def push(switch):
        for clock in range(clock_count):
            if linked[switch][clock] == 'x':
                clocks[clock] += 3
                if clocks[clock] == 15:
                    clocks[clock] = 3

    def solve(switch):

        print('solve = switch:{}'.format(switch))

        # 스위치를 전체를 다 시도해 봤다면
        if switch == switch_count:
            return 0 if aligned() else sys.maxsize

        ret = sys.maxsize
        for i in range(4):
            ret = min(ret, i + solve(switch + 1))
            push(switch)

        return ret

    return solve(0)


if __name__ == '__main__':

    cs = [12, 6, 6, 6, 6, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
    r = solution(cs)
    print(r)
    if r == 2:
        print('ok')

    cs = [12, 9, 3, 12, 6, 6, 9, 3, 12, 9, 12, 9, 12, 12, 6, 6]
    r = solution(cs)
    print(r)
    if r == 9:
        print('ok')
