import sys
sys.setrecursionlimit(10 ** 6)


def solution(n):
    ans = [[0 for _ in range(i + 1)] for i in range(n)]
    ans[0][0] = 1
    dfs(ans, 1, (0, 0, -1))
    return [e for row in ans for e in row]


def dfs(arr, value: '이전까지 채워진 수', args: '[prev_r, prev_c, prev_direction]'):
    r, c, d = args
    d = (args[2] + 1) % 3
    if d == 0:
        while r + 1 < len(arr) and arr[r + 1][c] == 0:
            r += 1
            value += 1
            arr[r][c] = value
    elif d == 1:
        while c + 1 < len(arr) and arr[r][c + 1] == 0:
            c += 1
            value += 1
            arr[r][c] = value
    else:
        while r > 0 and c > 0 and arr[r - 1][c - 1] == 0:
            r -= 1
            c -= 1
            value += 1
            arr[r][c] = value
    if args[:-1] != (r, c): dfs(arr, value, (r, c, d))


def solution2(n):
    ans = [[0] * i for i in range(1, n + 1)]
    dr, dc = (1, 0, -1), (0, 1, -1)
    r, c, d = 0, 0, 0
    value, limit = 1, (n + 1) * n // 2
    while value <= limit:
        ans[r][c] = value
        nr, nc = r + dr[d], c + dc[d]
        value += 1
        if 0 <= nr < n and 0 <= nc <= nr and ans[nr][nc] == 0: r, c= nr, nc
        else:
            d = (d + 1) % 3
            r += dr[d]
            c += dc[d]
    return [e for row in ans for e in row]


print(solution2(4))