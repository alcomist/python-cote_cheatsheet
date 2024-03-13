import math


def solution(n, words):
    answer = [0, 0]
    visited = []

    prev = ''
    for i, word in enumerate(words):
        order = i % n + 1
        if word in visited or (prev and prev[-1] != word[0]):
            answer = [order, math.ceil((i+1) / n)]
            break
        prev = word
        visited.append(word)

    return answer

if __name__ == "__main__":
    n = 3
    ws = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    r = solution(n, ws)
    print(r)
    if r == [3, 3]:
        print('ok')

    n = 5
    ws = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    r = solution(n, ws)
    print(r)
    if r == [0, 0]:
        print('ok')

    n = 2
    ws = ["hello", "one", "even", "never", "now", "world", "draw"]
    r = solution(n, ws)
    print(r)
    if r == [1, 3]:
        print('ok')

