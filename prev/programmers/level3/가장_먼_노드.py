def solution(n, edge):
    visited = [False] * (n + 1)
    arr = [[] for _ in range(n + 1)]

    for (a, b) in edge:
        arr[a].append(b)
        arr[b].append(a)

    return bfs(arr, visited)


def bfs(arr, visited):
    q = [1]
    visited[1] = True

    answer = 0
    while q:
        answer = len(q)
        size = len(q)

        while size:
            curr = q.pop(0)
            for next in arr[curr]:
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
            size -= 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))