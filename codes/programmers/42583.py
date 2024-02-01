import collections


def solution(bridge_length, weight, truck_weights):

    d = collections.deque([0] * bridge_length)

    truck_count = len(truck_weights)
    trucks = []

    answer = 0
    while truck_weights:

        answer += 1
        popped = d.popleft()
        if popped:
            weight += popped
            trucks.append(popped)

        truck_weight = truck_weights[0]
        if truck_weight <= weight:
            weight -= truck_weight
            d.append(truck_weight)
            truck_weights = truck_weights[1:]
        else:
            d.append(0)

    while len(trucks) < truck_count:
        popped = d.popleft()
        answer += 1
        if popped:
            trucks.append(popped)

    return answer


if __name__ == '__main__':

    bl = 2
    w = 10
    ws = [7, 4, 5, 6]

    r = solution(bl, w, ws)
    print(r)
    if r == 8:
        print('ok')

    bl = 100
    w = 100
    ws = [10]

    r = solution(bl, w, ws)
    print(r)
    if r == 101:
        print('ok')

    bl = 100
    w = 100
    ws = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    r = solution(bl, w, ws)
    print(r)
    if r == 110:
        print('ok')
