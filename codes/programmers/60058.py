def solution(p):

    def paren_type(s):

        paren_sum = 0
        temp = []
        for c in s:
            if c == '(':
                paren_sum += 1
                temp.append(c)
            elif c == ')':
                paren_sum -= 1
                if temp and temp[-1] == '(':
                    temp.pop()
                else:
                    temp.append(c)

        if paren_sum != 0:
            return -1
        else:
            if temp:
                return 0
            return 1

    def reverse_paren(s):
        # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        temp = []
        for i in range(0, len(s)):
            if s[i] == '(':
                temp.append(')')
            else:
                temp.append('(')
        return ''.join(temp)

    def modify(s):
        if paren_type(s) == 1:
            return s

        if not s or len(s) == 0:
            return ''

        for i in range(2, len(s)+1, 2):

            u = s[:i]
            ptype = paren_type(u)
            if ptype == -1:
                continue
            else:
                v = s[i:]

                if ptype == 1:
                    return u + modify(v)
                else:
                    return '(' + modify(v) + ')' + reverse_paren(u[1:-1])

    return modify(p)



if __name__ == '__main__':

    p = "(()())()"
    r = solution(p)
    print(r)
    if r == "(()())()":
        print('ok')

    p = ")("
    r = solution(p)
    print(r)
    if r == "()":
        print('ok')

    p = "()))((()"
    r = solution(p)
    print(r)
    if r == "()(())()":
        print('ok')

