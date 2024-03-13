from collections import deque

def solution(people, limit):

    answer = 0

    people = deque(sorted(people))

    while people:

        p = people.pop()
        if len(people) > 0 and p + people[0] <= limit:
            people.popleft()
        answer += 1

    return answer




if __name__ == '__main__':
    ps = [70, 50, 80, 50]
    l = 100
    r = solution(ps, l)
    if r == 3:
        print('ok')

    ps = [70, 80, 50]
    l = 100
    r = solution(ps, l)
    if r == 3:
        print('ok')
