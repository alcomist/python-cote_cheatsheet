import math

def solution(n, k):
    answer = 0

    def prime_check(n):  # n이 소수인지 아닌지 판별
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def convert(n, base):
        T = "0123456789ABCDEF"
        q, r = divmod(n, base)

        return convert(q, base) + T[r] if q else T[r]

    b = convert(n, k)

    for bb in b.split('0'):
        if not bb:
            continue
        if prime_check(int(bb)):
            answer += 1

    return answer


if __name__ == '__main__':

    n = 437674
    k = 3
    r = solution(n, k)
    if r == 3:
        print('ok')

    n = 110011
    k = 10
    r = solution(n, k)
    if r == 2:
        print('ok')
