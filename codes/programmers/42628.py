def solution(operations):
    answer = []
 
    for operation in operations:

        command, num = operation.split(" ")
        num = int(num)
 
        if command == "I":
            answer.append(num)
        elif command == "D" and num == 1 and answer:
            answer.remove(max(answer))
        elif command == "D" and num == -1 and answer:
            answer.remove(min(answer))
 
    if not answer:
        answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]
    return answer


if __name__ == "__main__":
    ops = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    r = solution(ops)
    if r == [0, 0]:
        print('ok')

    ops = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    r = solution(ops)
    if r == [333, -45]:
        print('ok')
