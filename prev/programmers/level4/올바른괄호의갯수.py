def solution(n):
    return dfs(0, 1, n)


def dfs(prev, depth, n):
    if depth > n: return 1
    res = 0
    for i in range(prev + 1, depth * 2):
        res += dfs(i, depth + 1, n)
    return res


def solution2(n):
    from math import factorial as f
    return f(2 * n) // (f(n) ** 2 * (n + 1))


def solution3(n):
    memo = {0: 1, 1: 1, 2: 2}
    b = 0
    if n >= 3:
        if n not in memo:
            for k in range(1, n + 1):
                b = b + (solution3(k - 1) * solution3(n - k))
            memo[n] = b
    return memo[n]


print(solution3(5))