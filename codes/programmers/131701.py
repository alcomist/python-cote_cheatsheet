from collections import deque

def solution(elements):
    answer = set()

    for i in range(1, len(elements)+1):

        d = deque(elements)
        for j in range(0, len(elements)):
            answer.add(sum(list(d)[0:i]))
            d.rotate(1)

    return len(answer)


if __name__ == "__main__":
    es = [7, 9, 1, 1, 4]
    r = solution(es)
    if r == 18:
        print('ok')
