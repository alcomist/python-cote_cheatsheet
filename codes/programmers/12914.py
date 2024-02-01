def solution(n):

    a = [0] * (n+1)

    a[0] = 1
    a[1] = 1
    for i in range(2, n+1):
        a[i] += (a[i-1] + a[i-2])

    #print(a)

    return a[n]%1234567


if __name__ == '__main__':

    n = 4
    r = solution(n)
    if r == 5:
        print('ok')

    n = 3
    r = solution(n)
    if r == 3:
        print('ok')
