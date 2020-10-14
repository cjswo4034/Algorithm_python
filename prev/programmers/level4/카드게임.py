import sys

sys.setrecursionlimit(10000)


def solution(left, right):
    dp = [[-1 for _ in range(5)] for _ in range(5)]
    return dfs(dp, left, right, 0, 0)


def solution2(left, right):
    map_list = [[-1 for j in range(len(right)+1)] for i in range(len(left)+1)]
    map_list[0][0] = 0

    for i in range(len(left)):
        for j in range(len(right)):
            if map_list[i][j] != -1:
                if left[i] > right[j]:
                    map_list[i][j] += right[j]
                    map_list[i][j + 1] = max(map_list[i][j], map_list[i][j + 1])
                else:
                    map_list[i + 1][j + 1] = max(map_list[i][j], map_list[i+1][j])
                    map_list[i + 1][j] = map_list[i][j]

    max_value = 0
    for i in range(len(left)):
        max_value = max(max_value, map_list[len(left)-1][i], map_list[i][len(right)-1])

    return max_value


def dfs(dp, left, right, l, r):
    if l == len(left) or r == len(right): return 0
    if dp[l][r] != -1: return dp[l][r]

    dp[l][r] = 0
    if left[l] > right[r]:
        dp[l][r] = dfs(dp, left, right, l, r + 1) + right[r]

    dp[l][r] = max(
        dp[l][r],
        dfs(dp, left, right, l + 1, r),
        dfs(dp, left, right, l + 1, r + 1))
    return dp[l][r]


print(solution([3, 2, 5], [2, 4, 1]))