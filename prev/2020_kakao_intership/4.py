def solution(board):
    return bfs(board)


# 건설하려는 도로가 이미 건설된 도로보다 비용이 적을 때 건설할 수 있다.
def bfs(board):
    costs = [[[987654321, 987654321] for i in range(len(board))] for i in range(len(board))]
    costs[0][0] = [0, 0]
    q = [[0, 0, 0], [0, 0, 1]]                      # [row, col, direction] direction - 0: 수평이동, 1: 상하이동
    direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # 좌우: 0, 상하: 1

    while q:
        current = q.pop(0)
        for i, d in enumerate(direction):
            n_row = current[0] + d[0]
            n_col = current[1] + d[1]
            if n_row < 0 or n_col < 0 or n_row >= len(board) or n_col >= len(board) or board[n_row][n_col]: continue
            
            n_cost = costs[current[0]][current[1]][current[2]] + 100
            if current[2]:
                n_cost += 500 if not i // 2 else 0  # 상하, 좌우이동하면 코너
            else: 
                n_cost += 500 if i // 2 else 0      # 수평, 상하이동하면 코너
            
            # 다음 구간이 원래 구간보다 비용이 더 크면 건설X
            if n_cost > costs[n_row][n_col][i // 2]: continue

            costs[n_row][n_col][i // 2] = n_cost
            q.append([n_row, n_col, i // 2])
            
        for c in costs:
            print(c)
        print('-------------------------------')
    return min(costs[-1][-1])


print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))