def solution(n, l, r):

    cantore = "1"

    for i in range(1, n+1):

        t = ""
        for c in cantore:
            if c == "1":
                t += "11011"
            else:
                t += "00000"
        cantore = t
    answer = cantore[l-1:r].count("1")
    #print(answer)
    return answer


if __name__ == '__main__':

    n = 2
    l = 4
    r = 17

    a = solution(n, l, r)
    if a == 8:
        print('ok')