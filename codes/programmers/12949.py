def solution(arr1, arr2):

    len_i = len(arr1)
    len_k = len(arr2)
    len_j = len(arr2[0])

    answer = [[0] * len_j for _ in range(len_i)]
    for i in range(len_i):
        for j in range(len_j):
            for k in range(len_k):
                answer[i][j] += arr1[i][k] * arr2[k][j]
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
