n, m = map(int, input().split())

def solve(n, m):

    visited = [n]
    seed = n

    while True:
        seed = sum([pow(x, m) for x in map(int, list(str(seed)))])
        if seed in visited:
            break
        visited.append(seed)

    visited = visited[:visited.index(seed)]

    #print(seed)
    #print(' '.join(map(str, visited)))
    print(len(visited))


solve(n, m)