def solution(board):
    answer, n = [], len(board)
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited = [[987654321] * n for _ in range(n)]
    visited[0][0] = 0
    q = [[0, 0, 0, 1], [0, 0, 0, 0]]

    while q:
        r, c, cost, d = q.pop(0)
        for i in range(4):
            nr = r + direction[i][0]
            nc = c + direction[i][1]

            if nr < 0 or nc < 0 or nr >= n or nc >= n: continue
            if board[nr][nc] or abs(i - d) == 2: continue

            n_cost = cost + (100 if i == d else 600)

            if visited[nr][nc] < n_cost: continue
            visited[nr][nc] = n_cost
            q.append([nr, nc, n_cost, i])

    return visited[-1][-1]
    
# 지점에 도착했을 때 비용이 적게든 것이 우선순위
# 이전 지점 방향 기억해야됨

print(solution([
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]))