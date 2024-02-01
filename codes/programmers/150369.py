def solution(cap, n, deliveries, pickups):
    answer = 0

    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    delivery_count = 0
    pickup_count = 0

    for i in range(n):
        delivery_count += deliveries[i]
        pickup_count += pickups[i]

        while delivery_count > 0 or pickup_count > 0:
            delivery_count -= cap
            pickup_count -= cap

            answer += (n-i)*2

    return answer


if __name__ == '__main__':

    c = 4
    n = 5
    ds = [1, 0, 3, 1, 2]
    ps = [0, 3, 0, 4, 0]

    r = solution(c, n, ds, ps)
    print(r)
    if r == 16:
        print('ok')

    c = 2
    n = 7
    ds = [1, 0, 2, 0, 1, 0, 2]
    ps = [0, 2, 0, 1, 0, 2, 0]

    r = solution(c, n, ds, ps)
    print(r)
    if r == 30:
        print('ok')
