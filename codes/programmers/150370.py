def solution(today, terms, privacies):
    answer = []

    days_in_month = 28
    term_dic = {term[0]: int(term[2:]) for term in terms}

    def get_days(s):
        y, m, d = map(int, s.split('.'))
        return (y*days_in_month*12) + (m*days_in_month) + d

    today_total = get_days(today)

    for index, privacy in enumerate(privacies):
        a, b = privacy.split()
        total = get_days(a) + term_dic[b]*days_in_month

        if total <= today_total:
            answer.append(index+1)

    return answer


if __name__ == '__main__':

    t = "2022.05.19"
    ts = ["A 6", "B 12", "C 3"]
    ps = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

    r = solution(t, ts, ps)
    print(r)
    if r == [1, 3]:
        print('ok')

