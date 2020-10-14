def solution(maps):
    return bfs(maps, [0, 0])


def bfs(maps, start):
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = [start]
    maps[start[0]][start[1]] = 0

    res = 0
    while q:
        res += 1
        size = len(q)
        while size:
            curr = q.pop(0)
            if curr[0] == len(maps) - 1 and curr[1] == len(maps[0]) - 1: return res
            for d in dir:
                nr = curr[0] + d[0]
                nc = curr[1] + d[1]

                if nr < 0 or nc < 0 or nr >= len(maps) or nc >= len(maps[0]): continue
                if not maps[nr][nc]: continue
                maps[nr][nc] = 0
                q.append([nr, nc])
            size -= 1
    return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))