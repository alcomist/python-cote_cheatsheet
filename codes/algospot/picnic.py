# 6.3 문제: 소풍 (문제 ID: PICNIC, 난이도: 하)

def solution(n, pairs):

    taken = [False] * n

    friends = [[False for _ in range(n)] for _ in range(n)]

    # friends는 1->0이 친구면 0->1도 친구이다
    for pair in pairs:
        friends[pair[0]][pair[1]] = True
        friends[pair[1]][pair[0]] = True

    def dfs(n):
        first_free = -1
        for i in range(n):
            if not taken[i]:
                first_free = i
                break

        # 모두 다 짝지어져 있다면 1을 리턴
        if first_free == -1:
            return 1

        ret = 0
        for pair_with in range(first_free+1, n):
            if not taken[pair_with] and friends[first_free][pair_with]:
                taken[first_free] = True
                taken[pair_with] = True
                ret += dfs(n)
                taken[first_free] = False
                taken[pair_with] = False

        return ret

    return dfs(n)


if __name__ == '__main__':

    n = 4
    fs = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2], [1, 3]]
    r = solution(n, fs)
    print(r)
    if r == 3:
        print('ok')
