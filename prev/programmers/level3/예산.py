def solution(budgets, M):
    if sum(budgets) <= M: return max(budgets)
    budgets.sort()

    ans, l, r= 0, 0, max(budgets)
    while l <= r:
        m = int((l + r) / 2)
        total = get_sum(budgets, m)
        if total <= M:
            l = m + 1
            ans = max(ans, m)
        else:
            r = m - 1

    return ans


def get_sum(budgets, M):
    tot = 0
    for budget in budgets:
        tot += min(budget, M)
    return tot


print(solution([120, 110, 140, 150], 485))