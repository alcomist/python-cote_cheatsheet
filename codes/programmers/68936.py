def solution(arr):

    # 1 : b, 0 : w, -1 : divide
    def get_color(x, y, n):
        check = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != check:
                    return -1
        return check

    def compress(x, y, n):

        color = get_color(x, y, n)

        if color == -1:
            n //= 2

            result = '('
            result += compress(x, y, n)
            result += compress(x + n, y, n)
            result += compress(x, y + n, n)
            result += compress(x + n, y + n, n)
            result += ')'

            return result
        elif color == 1:
            return 'b'
        else:
            return 'w'

    compressed = compress(0, 0, len(arr))
    return [compressed.count('w'), compressed.count('b')]


if __name__ == "__main__":
    a = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
    r = solution(a)
    print(r)
    if r == [4, 9]:
        print('ok')

