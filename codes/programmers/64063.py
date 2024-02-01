import collections
import sys
sys.setrecursionlimit(10000000)

def iter_solution(k, room_number):
    room_dic = {}
    ret = []
    for i in room_number:
        n = i
        visit = [n]
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        ret.append(n)
        for j in visit:
            room_dic[j] = n+1
        print(room_dic)
    return ret

def solution(k, room_number):
    answer = []

    assign = collections.defaultdict(int)

    def find(x):
        if assign[x] == 0:
            assign[x] = x
            return x
        assign[x] = find(assign[x]+1)
        return assign[x]

    for room in room_number:

        num = assign[room]
        if num == 0:
            assign[room] = room
            answer.append(room)
        else:
            x = find(num)
            answer.append(x)

    return answer


if __name__ == '__main__':
    k = 10
    room_number = [1, 3, 4, 1, 3, 1]
    answer = iter_solution(k, room_number)
    print(answer)

