def solution(number, k):

    answer_len = len(number)-k
    answer = []

    for num in number:

        while k > 0 and answer and num > answer[-1]:
            answer.pop()
            k -= 1

        answer.append(num)

    return ''.join(answer)[:answer_len]


if __name__ == '__main__':
    n = "1924"
    k = 2
    r = solution(n, k)
    if r == '94':
        print('ok')

    n = "1231234"
    k = 3
    r = solution(n, k)
    if r == '3234':
        print('ok')

    n = "4177252841"
    k = 4
    r = solution(n, k)
    if r == '775841':
        print('ok')