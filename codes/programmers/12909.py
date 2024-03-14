def solution(s):

    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
            continue

        if stack and stack[-1] == '(':
            stack.pop()
            continue

        stack.append(c)

    return len(stack) == 0

if __name__ == '__main__':

    s = "()()"
    r = solution(s)
    if r:
        print('ok')

    s = "(())()"
    r = solution(s)
    if r:
        print('ok')

    s = ")()("
    r = solution(s)
    if not r:
        print('ok')

    s = "(()("
    r = solution(s)
    if not r:
        print('ok')
