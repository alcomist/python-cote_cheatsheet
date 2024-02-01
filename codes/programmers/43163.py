import collections

def solution(begin, target, words):

    def movable(a, b):
        return len([c for c in zip(a, b) if c[0] != c[1]]) == 1

    def bfs(begin, target, words):

        if target not in words:
            return 0

        dist = collections.defaultdict(int)

        queue = collections.deque()
        queue.append(begin)
        dist[begin] = 0

        while queue:

            top = queue.popleft()

            for word in words:
                if word not in dist and movable(top, word):
                    dist[word] = dist[top] + 1
                    queue.append(word)

        return dist[target]

    return bfs(begin, target, words)


if __name__ == '__main__':

    b = "hit"
    t = "cog"
    w = ["hot", "dot", "dog", "lot", "log", "cog"]

    r = solution(b, t, w)
    print(r)
    if r == 4:
        print('ok')

    b = "hit"
    t = "cog"
    w = ["hot", "dot", "dog", "lot", "log"]
    r = solution(b, t, w)
    print(r)
    if r == 0:
        print('ok')
