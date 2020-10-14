import sys
sys.setrecursionlimit(10000)


def solution(n):
    dp = [[-1, -1, -1] for _ in range(n)]
    return dfs(dp, 0, 0) if n % 2 == 0 else 0


# 0: ooo, 1:oox, 2:oxx
def dfs(dp, status, pos):
    if pos > len(dp): return 0
    if pos == len(dp): return 1 if status == 0 else 0
    if dp[pos][status] != -1: return dp[pos][status]

    dp[pos][status] = 0
    if status == 0:
        dp[pos][status] = dfs(dp, 2, pos) + dfs(dp, 1, pos + 1) + dfs(dp, 0, pos + 2)
    elif status == 1:
        dp[pos][status] = dfs(dp, 0, pos + 1) + dfs(dp, 2, pos + 1)
    else:
        dp[pos][status] = dfs(dp, 1, pos + 1)
    return dp[pos][status]


print(solution(2))