def solution(players, callings):

    po = {player: i for i, player in enumerate(players)}
    op = {i: player for i, player in enumerate(players)}

    for calling in callings:

        loc1 = po[calling]
        loc2 = loc1-1

        p2 = op[loc2]

        op[loc1] = p2
        op[loc2] = calling

        po[calling] = loc2
        po[p2] = loc1

    return list(op.values())





if __name__ == '__main__':
    ps = ["mumu", "soe", "poe", "kai", "mine"]
    cs = ["kai", "kai", "mine", "mine"]
    r = solution(ps, cs)
    if r == ["mumu", "kai", "mine", "soe", "poe"]:
        print('ok')