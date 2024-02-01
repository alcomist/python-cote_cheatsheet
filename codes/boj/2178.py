import sys

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, list(sys.stdin.readline().strip()))))


# board = [list(map(int, list(sys.stdin.readline()))) for _ in range(n)]

#print(board)

def solve(b, y, x, n, m):

    answer = [[0 for _ in range(m)] for _ in range(n)]

    visited = [(y, x)]
    answer[y][x] = 1

    q = [(y, x)]

    while q:

        cy, cx = q.pop(0)

        for dy, dx in [(cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)]:

            if 0 <= dy < n and 0 <= dx < m:
                if (dy, dx) not in visited:
                    if b[dy][dx] == 1:
                        visited.append((dy, dx))
                        answer[dy][dx] = answer[cy][cx] + 1
                        q.append((dy, dx))

    return answer[n-1][m-1]


print(solve(board, 0, 0, n, m))
