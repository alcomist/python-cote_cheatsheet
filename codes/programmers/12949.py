def solution(arr1, arr2):
    answer = [[]]

    def multiply(a1, a2):

        a = []
        for i in range(len(a1)):
            a.append(a1[i] * a2[i])

        return a

    for i, a in enumerate(arr1):
        for j, b in enumerate(arr2):

            print(i, j, a, b, multiply(a, b))
        print()


    return answer


if __name__ == '__main__':
    #a1 = [[1, 4], [3, 2], [4, 1]]
    #a2 = [[3, 3], [3, 3]]

    #r = solution(a1, a2)
    #if r == [[15, 15], [15, 15], [15, 15]]:
    #    print('ok')

    a1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    a2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

    r = solution(a1, a2)
    if r == [[22, 22, 11], [36, 28, 18], [29, 20, 14]]:
        print('ok')
