import collections
import itertools


def solution(user_ids, banned_ids):
    answer = 0

    d = collections.defaultdict(set)

    def candidate(bid, uid):
        if len(bid) != len(uid):
            return False

        for i in range(len(bid)):

            if bid[i] != '*' and bid[i] != uid[i]:
                return False

        return True

    for banned_id in banned_ids:
        for user_id in user_ids:
            if candidate(banned_id, user_id):
                d[banned_id].add(user_id)




if __name__ == '__main__':

    uid = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    bid = ["fr*d*", "abc1**"]

    r = solution(uid, bid)
    print(r)
    if r == 2:
        print('ok')

    uid = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    bid = ["*rodo", "*rodo", "******"]

    r = solution(uid, bid)
    print(r)
    if r == 2:
        print('ok')

    uid = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    bid = ["fr*d*", "*rodo", "******", "******"]
    r = solution(uid, bid)
    print(r)
    if r == 3:
        print('ok')

