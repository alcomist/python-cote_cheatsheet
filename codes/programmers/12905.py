def solution(board):
    answer = 1234

    return answer


if __name__ == '__main__':

    bs = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
    r = solution(bs)
    if r == 9:
        print('ok')

    bs = [[0,0,1,1],[1,1,1,1]]
    r = solution(bs)
    if r == 4:
        print('ok')

