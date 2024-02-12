

def solution(n):

    if n == 1:
        return 1
    if n == 2:
        return 2

    return solution(n - 1) + solution(n - 2)


if __name__ == '__main__':

    r = solution(5)
    print(r)
    if r == 25:
        print('ok')
