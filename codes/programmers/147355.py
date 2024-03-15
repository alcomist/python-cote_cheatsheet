def solution(t, p):
    answer = 0
    tlen = len(t)
    plen = len(p)
    pval = int(p)

    for i in range(0, tlen-plen+1):
        #print(int(t[i:i + plen]))
        if int(t[i:i+plen]) <= pval:
            answer += 1

    return answer


if __name__ == '__main__':

    t = "3141592"
    p = "271"
    r = solution(t, p)
    if r == 2:
        print('ok')

    t = "500220839878"
    p = "7"
    r = solution(t, p)
    if r == 8:
        print('ok')

    t = "10203"
    p = "15"
    r = solution(t, p)
    if r == 3:
        print('ok')

