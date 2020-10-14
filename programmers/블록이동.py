def solution(board):
    answer = 0
    return bfs(board)


def bfs(board):
    res, dest = 0, (len(board) - 1, len(board) - 1)
    q = [((0, 0), (0, 1))]

    visited = [[[] for c in range(len(board))] for r in range(len(board))]
    visited[0][0].append((0, 1))
    visited[0][1].append((0, 0))

    while q:
        size = len(q)
        while size > 0:
            size -= 1
            p1, p2 = q.pop(0)
            if p1 == dest or p2 == dest: return res
            for np1, np2 in get_all_rotated_pos(board, p1, p2):
                if np2 in visited[np1[0]][np1[1]] or np1 in visited[np2[0]][np2[1]]: continue
                visited[np1[0]][np1[1]].append(np2)
                visited[np2[0]][np2[1]].append(np1)
                q.append((np1, np2))
        res += 1
    return res

def get_all_rotated_pos(board, p1, p2):
    res = set()
    move(board, p1, p2, res)
    rotate(board, p1, p2, res)
    rotate(board, p2, p1, res)
    return res

def rotate(board, p1, p2, res):
    if p1[0] == p2[0]:
        nr, nc = p1[0] + 1, p1[1]
        if nr < len(board) and not (board[nr][p2[1]] or board[nr][nc]): res.add((p1, (nr, nc)))
        nr = p1[0] - 1
        if nr >= 0 and not (board[nr][p2[1]] or board[nr][nc]): res.add((p1, (nr, nc)))
    elif p1[1] == p2[1]:
        nr, nc = p1[0], p1[1] + 1
        if nc < len(board) and not (board[p2[0]][nc] or board[nr][nc]): res.add((p1, (nr, nc)))
        nc = p1[1] - 1
        if nc >= 0 and not (board[p2[0]][nc] or board[nr][nc]): res.add((p1, (nr, nc)))

def move(board, p1, p2, res):
    (r1, c1), (r2, c2) = p1, p2
    for d in direction2:
        nr1, nr2 = r1 + d[0], r2 + d[0]
        nc1, nc2 = c1 + d[1], c2 + d[1]
        if nr1 >= len(board) or nc1 >= len(board) or nr1 < 0 or nc1 < 0: continue
        if nr2 >= len(board) or nc2 >= len(board) or nr2 < 0 or nc2 < 0: continue

        if r1 == r2 and (board[nr1][nc1] or board[nr1][nc2]): continue
        if c1 == c2 and (board[nr1][nc1] or board[nr2][nc1]): continue

        res.add(((nr1, nc1), (nr2, nc2)))

direction1 = [[-1, 0], [0, 1], [1, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
direction2 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
print(solution([
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[1, 1, 1, 1, 1, 1, 1, 0, 0], 
[1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 1, 1, 1, 1, 0, 0], 
[0, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 0, 1, 1, 1, 1, 1, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[1, 1, 1, 1, 1, 1, 1, 1, 0]]))