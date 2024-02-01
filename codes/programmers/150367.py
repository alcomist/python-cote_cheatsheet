def solution(numbers):
    answer = []

    def get_padded_string(s):

        i = 0
        slen = len(s)
        while True:
            if 2**i <= slen < 2**(i+1):
                break
            i += 1

        pad = 2**(i+1)-1 - slen
        if pad == 0:
            return s
        return s.rjust(len(s) + pad, '0')

    def is_tree(s):

        if len(s) == 1:
            return True

        mid = len(s) // 2
        if s[mid] == '0':
            if '1' in s:
                return False

        return is_tree(s[:mid]) and is_tree(s[mid+1:])

    for number in numbers:
        binary = bin(number)[2:]
        binary = get_padded_string(binary)
        if is_tree(binary):
            answer.append(1)
        else:
            answer.append(0)

    return answer


if __name__ == '__main__':
    n = [7, 42, 5]
    r = solution(n)
    print(r)
    if r == [1, 1, 0]:
        print('ok')

    n = [63, 111, 95]
    r = solution(n)
    print(r)
    if r == [1, 1, 0]:
        print('ok')
