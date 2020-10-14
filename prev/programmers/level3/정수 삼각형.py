def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            l = r = 0
            if j - 1 >= 0:
                l = triangle[i - 1][j - 1]
            if len(triangle[i - 1]) > j:
                r = triangle[i - 1][j]
            triangle[i][j] += max(l, r)

    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))