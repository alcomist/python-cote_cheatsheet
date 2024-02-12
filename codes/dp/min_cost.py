# 최소비용 구하기
# M x N 크기의 2차원의 비용 행렬의 출발셀과 도착셀을 포함한 모든 셀의 비용의 합
# dp 풀이

def solution(cost):

    mem = [[0 for _ in range(len(cost[0]) + 1)] for _ in range(len(cost) + 1)]

    def solve(y, x):

        for i in range(x):
            mem[0][i] = mem[0][i-1] + cost[0][i]
        for j in range(y):
            mem[j][0] = mem[j-1][0] + cost[j][0]

        for i in range(1, y):
            for j in range(1, x):
                mem[i][j] = min(mem[i-1][j], mem[i][j-1]) + cost[i][j]

        return mem[y-1][x-1]

    return solve(len(cost), len(cost[0]))


if __name__ == '__main__':

    c = [
        [1, 3, 5, 8],
        [4, 2, 1, 7],
        [4, 3, 2, 3]
    ]

    r = solution(c)
    print(r)
    if r == 12:
        print('ok')

