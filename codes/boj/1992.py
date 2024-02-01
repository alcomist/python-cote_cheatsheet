import sys

n = int(input())
#board = [sys.stdin.readline().strip() for _ in range(n)]
board = [list(input().strip()) for _ in range(n)]

#print(board)

def compress(y, x, n):

    if n == 1:
        return board[y][x]

    target = board[y][x]
    result = ''
    for dy in range(y, y + n):
        for dx in range(x, x + n):
            if target != board[dy][dx]:
                n = n // 2
                result += "("
                result += compress(y, x, n)
                result += compress(y, x + n, n)
                result += compress(y + n, x, n)
                result += compress(y + n, x + n, n)
                result += ")"
                return result
    return target


result = compress(0, 0, n)

if result == '((110(0101))(0010)1(0001))':
    print('YESSSSS~~~')

print(result)
