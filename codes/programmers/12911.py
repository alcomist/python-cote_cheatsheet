
# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
def solution(n):

    answer = 0

    zc = bin(n).count('1')

    while True:

        n += 1
        if bin(n).count('1') == zc:
            answer = n
            break

    return answer


if __name__ == '__main__':

    n = 78
    r = solution(n)
    if r == 83:
        print('ok')

    n = 15
    r = solution(n)
    if r == 23:
        print('ok')
