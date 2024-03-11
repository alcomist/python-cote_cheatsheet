def solution(s):

    t = 0
    z = 0

    while s != '1':
        z += s.count('0')
        t += 1
        s = s.replace('0', '')
        s = bin(len(s))[2:]

    return [t, z]


if __name__ == '__main__':

    ss = "110010101001"

    r = solution(ss)
    if r == [3, 8]:
        print('ok')

    ss = "01110"
    r = solution(ss)
    if r == [3, 3]:
        print('ok')

    ss = "1111111"
    r = solution(ss)
    if r == [4, 1]:
        print('ok')
