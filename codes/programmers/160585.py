def solution(board):

    answer = -1
    return answer


if __name__ == '__main__':

    bs = ["O.X", ".O.", "..X"]
    r = solution(bs)
    if r == 1:
        print('ok')


    bs = ["OOO", "...", "XXX"]
    r = solution(bs)
    if r == 0:
        print('ok')

    bs = ["...", ".X.", "..."]
    r = solution(bs)
    if r == 0:
        print('ok')

    bs = ["...", "...", "..."]
    r = solution(bs)
    if r == 1:
        print('ok')