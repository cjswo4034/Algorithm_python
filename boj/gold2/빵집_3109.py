import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
d = [-1, 0, 1]

def dfs(r, c):
    if arr[r][c] == 'x': return False
    arr[r][c] = 'x'

    if c == m - 1: return 1

    for dd in d:
        nr = r + dd
        if 0 <= nr and nr < n and dfs(nr, c + 1): 
            return True
    return False

answer = 0
for r in range(n):
    if dfs(r, 0): answer += 1
print(answer)