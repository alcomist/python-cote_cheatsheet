def solution(sizes):

    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]

    zipped = list(zip(*sizes))

    return max(zipped[0]) * max(zipped[1])


if __name__ == '__main__':
    ss = [[60, 50], [30, 70], [60, 30], [80, 40]]
    r = solution(ss)
    if r == 4000:
        print('ok')
