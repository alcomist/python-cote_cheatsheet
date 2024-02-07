# 고전 컴퓨터 알고리즘 인 파이썬 코드
def hanoi(start, transit, end, n):
    if n <= 0:
        return

    hanoi(start, end, transit, n-1)
    print(f"{n}번째 원반을 '{start}' 에서 '{transit}'으로 이동")
    hanoi(end, transit, start, n-1)


# C로 배우는 알고리즘 코드
def hanoi2(n, start, transit, end):
    if n == 1:
        print(f"{n}번째 원반을 '{start}' 에서 '{end}'으로 이동")
    else:
        hanoi2(n-1, start, end, transit)
        print(f"{n}번째 원반을 '{start}' 에서 '{end}'으로 이동")
        hanoi2(n-1, transit, start, end)


if __name__ == '__main__':
    #hanoi('1번 기둥', '2번 기둥', '3번 기둥', 3)
    hanoi2(3, '1번 기둥', '2번 기둥', '3번 기둥')
