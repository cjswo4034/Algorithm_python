direction = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}


def solution(dirs):
    visited = [[[] for _ in range(11)] for _ in range(11)]
    return dfs(5, 5, 0, dirs, visited)


def dfs(x, y, depth, cmd, visited):
    if depth >= len(cmd): return 0

    nx, ny = rotate(x, y, cmd[depth])
    if nx < 0 or ny < 0 or nx > 10 or ny > 10:
        return dfs(x, y, depth + 1, cmd, visited)

    res = 0
    if [x, y] not in visited[nx][ny] and [nx, ny] not in visited[x][y]:
        visited[nx][ny].append([x, y])
        visited[x][y].append([nx, ny])
        res = 1
    return res + dfs(nx, ny, depth + 1, cmd, visited)


def rotate(x, y, direct):
    return x + direction[direct][0], y + direction[direct][1]


print(solution("LURDLURD"))
print(solution("ULURRDLLU"))