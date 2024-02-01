import itertools

def solution(coin, cards):

    score = max(cards)+1

    user_cards = set(cards[:len(cards)//3])
    draw_cards = set()

    cards = cards[len(cards)//3:]

    round = 0

    #print(user_cards)
    #print(cards)

    while cards:

        # 2개를 무조건 뽑기
        a, b = cards[0], cards[1]

        # 남은 카드
        cards = cards[2:]

        round += 1

        draw_cards.add(a)
        draw_cards.add(b)

        found = False
        for card in user_cards:
            if score - card in user_cards:
                user_cards.remove(card)
                user_cards.remove(score-card)
                found = True
                break

        if found:
            continue

        found = False
        for card in user_cards:
            if score - card in draw_cards and coin > 0:
                user_cards.remove(card)
                draw_cards.remove(score-card)
                found = True
                coin -= 1
                break

        if found:
            continue

        found = False

        for card in draw_cards:
            if score - card in draw_cards and coin >= 2:
                draw_cards.remove(card)
                draw_cards.remove(score-card)
                coin -= 2
                found = True
                break

        if found:
            continue

        break

    return round


if __name__ == '__main__':

    coin = 4
    cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
    r = solution(coin, cards)
    print(r)
    if r == 5:
        print('ok')

    coin = 3
    cards = [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]
    r = solution(coin, cards)
    print(r)
    if r == 2:
        print('ok')

    coin = 2
    cards = [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]
    r = solution(coin, cards)
    print(r)
    if r == 4:
        print('ok')

    coin = 10
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    r = solution(coin, cards)
    print(r)
    if r == 1:
        print('ok')
