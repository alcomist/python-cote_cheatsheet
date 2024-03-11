def solution(book_time):
    minutes = 60 * 24
    total = [0] * minutes

    def time2digit(s):
        return int(s[:2]) * 60 + int(s[3:])

    for t in book_time:
        s = time2digit(t[0])
        e = time2digit(t[1]) + 10

        if e > minutes:
            e = minutes

        for i in range(s, e):
            total[i] += 1

    return max(total)

if __name__ == '__main__':
    bt = [
        ["15:00", "17:00"],
        ["16:40", "18:20"],
        ["14:20", "15:20"],
        ["14:10", "19:20"],
        ["18:20", "21:20"]
    ]
    r = solution(bt)
    if r == 3:
        print('ok')

    bt = [["09:10", "10:10"], ["10:20", "12:20"]]
    r = solution(bt)
    if r == 1:
        print('ok')

    bt = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
    r = solution(bt)
    if r == 3:
        print('ok')
