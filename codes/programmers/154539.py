from collections import deque
def solution(numbers):
    answer = []

    st = []

    for number in numbers:
        for i in range(len(st)-1, -1, -1):
            if st[i][1] == -1 and st[i][0] < number:
                st[i][1] = number

        st.append([number, -1])

    for s in st:
        answer.append(s[1])
    return answer


if __name__ == '__main__':
    ns = [2, 3, 3, 5]
    r = solution(ns)
    if r == [3, 5, 5, -1]:
        print('ok')

    ns = [9, 1, 5, 3, 6, 2]
    r = solution(ns)
    if r == [-1, 5, 6, 6, -1, -1]:
        print('ok')
