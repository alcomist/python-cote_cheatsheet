#from collections import queue
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]

    def bfs(y, x, n, m):

        result = 0
        xs = [0, 0, -1, 1]
        ys = [-1, 1, 0, 0]

        q = [[y, x]]
        result += int(maps[y][x])
        visited[y][x] = True

        while q:
            ny, nx = q.pop(0)

            for i in range(4):
                dy, dx = ny + ys[i], nx + xs[i]

                if 0 <= dy < n and 0 <= dx < m and not visited[dy][dx] and maps[dy][dx] != 'X':
                    result += int(maps[dy][dx])
                    visited[dy][dx] = True
                    q.append([dy, dx])

        return result

    for y in range(n):
        for x in range(m):
            if maps[y][x] != 'X' and not visited[y][x]:
                answer.append(bfs(y, x, n, m))

    if not answer:
        return [-1]
    return sorted(answer)


if __name__ == '__main__':
    m = ["X591X", "X1X5X", "X231X", "1XXX1"]
    r = solution(m)
    if r == [1, 1, 27]:
        print('ok')
