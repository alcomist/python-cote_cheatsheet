
def solution(n, k, cmds):
    answer = ''

    st = [False] * n
    deletes = []

    for cmd in cmds:
        a, b = cmd[0:1], cmd[1:]
        if a == 'D':
            b = int(b)
        elif a == 'U':
            b = int(b)
        elif a == 'C':
            st[k] = True
            k += 1
            deletes.append(k)

        elif a == 'Z':
            if deletes:
                top = deletes.pop()
                st[top] = False

    print(st)
    return answer


if __name__ == '__main__':
    n = 8
    k = 2
    cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]

    r = solution(n, k, cmd)
    if r == "OOOOXOOO":
        print('ok')