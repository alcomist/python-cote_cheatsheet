import collections

def solution(queue1, queue2):

    q1 = collections.deque(queue1)
    q2 = collections.deque(queue2)

    s1 = sum(queue1)
    s2 = sum(queue2)

    answer = 0
    if s1 == s2:
        return answer


    max_len = len(queue1) * 3
    while s1 != s2 and answer <= max_len:
        if s1 > s2:
            n = q1.popleft()
            s1 -= n
            s2 += n
            q2.append(n)
        else:
            n = q2.popleft()
            s1 += n
            s2 -= n
            q1.append(n)

        answer += 1

    if answer > max_len:
        return -1
    return answer


if __name__ == '__main__':
    q1 = [3, 2, 7, 2]
    q2 = [4, 6, 5, 1]

    result = solution(q1, q2)
    if result == 2:
        print('ok')

    q1 = [1, 2, 1, 2]
    q2 = [1, 10, 1, 2]

    result = solution(q1, q2)
    if result == 7:
        print('ok')

    q1 = [1, 1]
    q2 = [1, 5]

    result = solution(q1, q2)
    if result == -1:
        print('ok')

