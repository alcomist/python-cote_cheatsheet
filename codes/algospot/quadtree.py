cols = rows = 100
decompressed = [['' for j in range(cols)] for i in range(rows)]


def decompress(str, y, x, size):

    head = str[0]
    temp = str[1:]
    if head == 'b' or head == 'w':
        for dy in range(size):
            for dx in range(size):
                decompressed[y+dy][x+dx] = head
    else:
        half = size//2
        temp = decompress(temp, y, x, half)
        temp = decompress(temp, y, x+half, half)
        temp = decompress(temp, y+half, x, half)
        temp = decompress(temp, y+half, x+half, half)

    return temp


if __name__ == '__main__':
    size = 16
    decompress('xxwwwbxwxwbbbwwxxxwwbbbwwwwbb', 0, 0, size)
    for y in range(size):
        for x in range(size):
            print(decompressed[y][x], end=' ')
        print()
