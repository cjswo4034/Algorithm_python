def solution(N, number):
    ans = dfs(N, number, 0, 0)

    if ans <= 8:
        return ans
    else:
        return -1


def dfs(n, number, curr, depth):
    if depth > 8 or (curr == 0 and depth > 0):
        return 987654321
    if curr == number:
        return depth

    next_n, next_depth = 0, depth
    ans = 987654321
    for i in range(8 - depth):
        next_n = next_n * 10 + n
        next_depth += 1
        ans = min(ans,
                  dfs(n, number, curr + next_n, next_depth),
                  dfs(n, number, curr - next_n, next_depth),
                  dfs(n, number, curr * next_n, next_depth),
                  dfs(n, number, curr // next_n, next_depth))
    return ans


print(solution(5, 12))
print(solution(2, 11))


# N + N
# N - N
# N * N
# N / N
# N * 10 + N
