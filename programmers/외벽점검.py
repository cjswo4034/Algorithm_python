### 시간초과 (자바는 통과)

def solution(n, weak, dist):
    if max(weak) - min(weak) <= max(dist): return 1
    args = [987654321]
    dist = sorted(dist, key=None, reverse=True)
    
    visited = [False for _ in range(len(weak))]
    weak.extend([w + n for w in weak])
    
    dfs(visited, weak, dist, 0, args)
    return args[0] if args[0] != 987654321 else -1

def dfs(visited, weak, dist, depth, args):
    if depth >= args[0]: return
    if False not in visited:
        args[0] = min(args[0], depth)
        return
    if depth == len(dist): return

    length = len(visited)
    for i in range(length):
        if visited[i]: continue
        pos = i
        while pos < len(weak) and not visited[pos % length] and \
            weak[pos] <= weak[i] + dist[depth]:
            visited[pos % length] = True
            pos += 1

        dfs(visited, weak, dist, depth + 1, args)

        for j in range(i, pos): visited[j % length] = False

print(solution(30, [0, 3, 11, 21], [10, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))