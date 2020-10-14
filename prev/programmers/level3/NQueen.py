def solution(n):
    row = [False for _ in range(n)]
    line = [[False, False] for _ in range(n * 3 + 1)]
    return n_queen(0, row, line)


def n_queen(n, row, line):
    if n == len(row): return 1

    ans = 0
    l = r = n + len(row)
    for i in range(len(row)):
        l -= 1
        r += 1
        if row[i] or line[l][0] or line[r][1]: continue

        line[l][0] = line[r][1] = row[i] = True
        ans += n_queen(n + 1, row, line)
        line[l][0] = line[r][1] = row[i] = False

    return ans


print(solution(10))