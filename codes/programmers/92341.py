import collections
import math

def solution(fees, records):
    answer = []

    default_time, default_price, unit_time, unit_price = fees

    record_dic = collections.defaultdict(list)
    record_time = collections.defaultdict(int)

    def get_minutes(s):
        h, m = s.split(':')
        return int(h) * 60 + int(m)

    for record in records:
        a, b, c = record.split()

        record_dic[b].append(get_minutes(a))

    for k, v in record_dic.items():
        if len(v) % 2:
            v.append(get_minutes('23:59'))

        temp = 0
        while v:
            b = v.pop()
            a = v.pop()
            temp += (b-a)

        temp = temp - default_time

        price = 0
        price += default_price

        if temp > 0:
            price += int(math.ceil(temp / unit_time)) * unit_price

        record_time[k] = price

    for k in sorted(record_time.keys()):
        answer.append(record_time[k])

    return answer


if __name__ == '__main__':

    f = [180, 5000, 10, 600]
    rs = ["05:34 5961 IN",
          "06:00 0000 IN",
          "06:34 0000 OUT",
          "07:59 5961 OUT",
          "07:59 0148 IN",
          "18:59 0000 IN",
          "19:09 0148 OUT",
          "22:59 5961 IN",
          "23:00 5961 OUT"]

    r = solution(f, rs)
    if r == [14600, 34400, 5000]:
        print('ok')

    f = [120, 0, 60, 591]
    rs = ["16:00 3961 IN",
          "16:00 0202 IN",
          "18:00 3961 OUT",
          "18:00 0202 OUT",
          "23:58 3961 IN"]

    r = solution(f, rs)
    if r == [0, 591]:
        print('ok')


    f = [1, 461, 1, 10]
    rs = ["00:00 1234 IN"]

    r = solution(f, rs)
    if r == [14841]:
        print('ok')