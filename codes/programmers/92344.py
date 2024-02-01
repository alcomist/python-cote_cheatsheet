import collections


def solution_slow(board, skills):
    answer = 0

    for skill in skills:
        t, y1, x1, y2, x2, degree = skill
        if t == 1:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    board[y][x] -= degree
        else:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    board[y][x] += degree

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] > 0:
                answer += 1

    return answer

def solution(board, skills):
    answer = 0

    degree_dic = collections.defaultdict(int)
    for skill in skills:
        t, y1, x1, y2, x2, degree = skill
        if t == 1:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    degree_dic[f'{y}:{x}'] -= degree
        else:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    degree_dic[f'{y}:{x}'] += degree

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] + degree_dic[f'{y}:{x}'] > 0:
                answer += 1

    return answer


if __name__ == '__main__':

    bs = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
    ss = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]

    r = solution(bs, ss)
    if r == 10:
        print('ok')

    bs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ss = [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]

    r = solution(bs, ss)
    if r == 6:
        print('ok')
