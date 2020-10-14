N, M, V = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    link = list(map(int, input().split()))
    arr[link[0]][link[1]] = 1
    arr[link[1]][link[0]] = 1


def dfs(curr, foot_prints):
    foot_prints += [curr]
    for search_node in range(len(arr[curr])):
        if arr[curr][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, foot_prints)

    return foot_prints


def bfs(start):
    q = [start]
    foot_prints = [start]

    while q.__len__() > 0:
        curr = q.pop(0)
        for next_node in range(len(arr[curr])):
            if arr[curr][next_node] and next_node not in foot_prints:
                foot_prints += [next_node]
                q += [next_node]
    return foot_prints


print(*dfs(V, []))
print(*bfs(V))

