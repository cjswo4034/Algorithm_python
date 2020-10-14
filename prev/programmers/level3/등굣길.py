def solution(m, n, puddles):
    map = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for puddle in puddles:
        map[puddle[1]][puddle[0]] = -1

    div = 1000000007
    map[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if map[i][j] < 0: continue
            if map[i - 1][j] < 0: map[i][j] += 1
            if map[i][j - 1] < 0: map[i][j] += 1
            map[i][j] = (map[i][j] + map[i - 1][j] + map[i][j - 1]) % div

    print(map)
    return map[n][m]


print(solution(4, 3, [[2, 1], [2, 2]]))