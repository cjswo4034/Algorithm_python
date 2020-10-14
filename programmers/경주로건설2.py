direction = [[0, -1], [-1, 0], [0, 1], [1, 0]]  # 0, 2: 가로  1, 3: 세로


def solution(board):
    """
    * (0, 0)에서 오른쪽으로 출발한 비용과 아래로 출발한 비용 중 낮은 값을 반환한다.

    :param board: 도면의 상태를 나타내는 2차원 행렬. (0: 빈공간, 1: 벽)
    :return: (0, 0)에서 (n, n)까지 경주로를 건설하는데 드는 최소비용.
    """
    N = len(board)
    visit = [[9876543210] * N for _ in range(N)]
    return min(dfs(board, visit, [0, 0, 2, 0]),  # 가로출발
               dfs(board, visit, [0, 0, 3, 0]))  # 세로출발


def dfs(board, visit, args):
    """
    * 다음에 방문할 지역의 비용이 계산 결과보다 낮으면 방문하지 않는다.
    * 현재 지역을 방문했을 때의 방향과 다음에 방문할 지역의 방향이 다르면 커브(600원!!)로 건설
    * 현재 지역을 방문했을 때의 반대 방향으로 못 돌아가므로 d != i일 때만 검사

    :param board: 2차원 행렬. (0: 빈공간, 1: 벽)
    :param visit: visit[r][c]: r행 c열을 방문했을 때 최소비용
    :param args: [r, c, d, cost] 직전 행, 열, 방문했을 때 방향, 비용
    :return: 경주로 건설 최소비용
    """
    r, c, d, cost = args[:]

    for i in range(4):
        nr = r + direction[i][0]
        nc = c + direction[i][1]

        is_curved = d != i
        n_cost = cost + (600 if is_curved else 100)

        if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board) or board[nr][nc]: continue
        if visit[nr][nc] < n_cost: continue

        visit[nr][nc] = n_cost
        dfs(board, visit, [nr, nc, i, n_cost])

    return visit[-1][-1]


print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
