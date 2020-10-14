def solution(tickets):
    tickets.sort()

    dict = {}
    answer = ["ICN"]
    visited = [False for _ in tickets]
    for i, ticket in enumerate(tickets):
        if not dict.get(ticket[0]):
            dict[ticket[0]] = []
        dict[ticket[0]].append([ticket[1], i])

    dfs(0, "ICN", visited, answer, dict)
    return answer


def dfs(depth, curr, visited, ans, dict):
    if depth >= len(visited) or not dict.get(curr):
        return depth == len(visited)

    for next in dict[curr]:
        if not visited[next[1]]:
            visited[next[1]] = True
            ans.append(next[0])
            if dfs(depth + 1, next[0], visited, ans, dict): return True
            visited[next[1]] = False
            ans.pop()


print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "BOO"], ["BOO", "ICN"]]))