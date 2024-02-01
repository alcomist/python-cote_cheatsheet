
def solution(n):

    board = [0] * (n+1)

    def promising(col):
        for i in range(col):
            if board[col] == board[i] or col-i == abs(board[col] - board[i]):
                return False

        return True

    def nqueen(col, n):

        count = 0
        if col == n:
            return 1

        for i in range(n):
            board[col] = i

            if promising(col):
                count += nqueen(col + 1, n)
        return count

    return nqueen(0, n)


if __name__ == '__main__':

    n = 4
    r = solution(n)
    if r == 2:
        print('ok')

    n = 12
    r = solution(n)
    print(r)
    if r == 2:
        print('ok')