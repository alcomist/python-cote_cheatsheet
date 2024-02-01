def solution(s):
    answer = ''

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    if len(s) < 2 or s == s[::-1]:
        return len(s)

    for i in range(len(s) - 1):
        answer = max(answer, expand(i, i+1), expand(i, i+2), key=len)

    return len(answer)


if __name__ == '__main__':

    s = "abcdcba"
    r = solution(s)
    if r == 7:
        print('ok')

    s = "abacde"
    r = solution(s)
    if r == 3:
        print('ok')