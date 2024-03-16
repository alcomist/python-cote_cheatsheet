def solution(wallpaper):

    minx, miny, maxx, maxy = 100, 100, 0, 0
    for i, w in enumerate(wallpaper):
        if w.count('#') > 0:
            miny = min(miny, i)
            maxy = max(maxy, i+1)

        for j, c in enumerate(w):
            if c == '#':
                minx = min(minx, j)
                maxx = max(maxx, j+1)

    #print(miny, minx, maxy, maxx)
    return [miny, minx, maxy, maxx]


if __name__ == '__main__':
    ws = [".#...", "..#..", "...#."]
    r = solution(ws)

    if r == [0, 1, 3, 4]:
        print('ok 1')

    ws = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
    r = solution(ws)
    if r == [1, 3, 5, 8]:
        print('ok 2')

    ws = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
    r = solution(ws)
    if r == [0, 0, 7, 9]:
        print('ok 3')

    ws = ["..", "#."]
    r = solution(ws)
    if r == [1, 0, 2, 1]:
        print('ok 4')