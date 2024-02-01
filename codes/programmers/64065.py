def solution(s):
    answer = []

    ts = []
    a = s.split('},{')
    for aa in a:
        ts.append(list(map(int, aa.replace('{{', '').replace('}}', '').split(','))))
    ts.sort(key=len)

    for t in ts:
        for tt in t:
            if tt not in answer:
                answer.append(tt)

    return answer


if __name__ == '__main__':

    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    r = solution(s)
    print(r)
    if r == [2, 1, 3, 4]:
        print('ok')

    s = "{{20,111},{111}}"
    r = solution(s)
    print(r)
    if r == [111, 20]:
        print('ok')