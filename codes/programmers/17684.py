import collections


def solution(msg):
    answer = []

    codes = {chr(c): c - ord('A')+1 for c in range(ord('A'), ord('Z')+1)}

    while True:

        #print(msg)
        if msg in codes:
            answer.append(codes[msg])
            break

        for i in range(1, len(msg)+1):
            sub_msg = msg[:i]
            if sub_msg not in codes:
                codes[sub_msg] = max(codes.values())+1
                answer.append(codes[msg[:i-1]])
                msg = msg[i-1:]
                break

    return answer



if __name__ == '__main__':

    m = 'KAKAO'
    r = solution(m)
    print(r)
    if r == [11, 1, 27, 15]:
        print('ok')

    m = 'TOBEORNOTTOBEORTOBEORNOT'
    r = solution(m)
    print(r)
    if r == [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]:
        print('ok')

    m = 'ABABABABABABABAB'
    r = solution(m)
    if r == [1, 2, 27, 29, 28, 31, 30]:
        print('ok')
