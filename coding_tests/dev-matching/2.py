# 10점 맞음
def solution(n, groups):
    res = n
    for i in range(1, len(groups) + 1):
        res = min(res, dfs(i, groups, [False] * len(groups), [False] * n, n) + i)
        print(i, res)
    return res


# depth 까지만 방문할 때 수동으로 꺼야될 전구의 수
def dfs(depth, groups, visit_group, visit, minimum):
    if depth == 0: return visit.count(0)

    res = 987654321
    for i in range(len(groups)):
        if visit_group[i]: continue
        s, e = groups[i]

        # 현재 그룹이 다 켜졌다면 방문하지 않는다.
        if visit[s - 1:e].count(0) == 0: continue
        visit_group[i] = True

        # 그룹이 킬 수 있는 전구를 다 킨다.
        for j in range(s - 1, e): visit[j] = True

        # 남은 전구 개수
        cost = visit.count(0)

        # 수동으로 끌 전구의 개수가 최소 횟수보다 크다면 방문하지 않는다.
        if minimum >= cost:
            minimum = cost
            res = min(res, dfs(depth - 1, groups, visit_group, visit, minimum))

        for j in range(s - 1, e): visit[j] = False
        visit_group[i] = False

    return res


print(solution(7, [[6, 7],[1, 4],[2, 4]]))