from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
arr = []
dir = [(1, 0, False), (-1, 0, False), (0, 1, False), (0, -1, False), (0, 0, True)]

def init(n, arr):
    pos_s, pos_e = [], []
    flag_s, flag_e = False, False
    for i in range(n):
        line = input()[:n]
        s, e = line.count('B'), line.count('E')
        if s:
            if s == 3: pos_s = (i, line.index('B') + 1, False)
            elif s == 1:
                if flag_s:
                    pos_s = (i, line.index('B'), True)
                    flag_s = False
                else: flag_s = True
        if e:
            if e == 3: pos_e = (i, line.index('E') + 1, False)
            elif e == 1:
                if flag_e:
                    pos_e = (i, line.index('E'), True)
                    flag_e = False
                else: flag_e = True
        line = line.replace('B', '0').replace('E', '0')
        arr.append(list(map(int, line)))
    return pos_s, pos_e

def check(arr, visit, pos, isRotate):
    if isRotate:
        r1, r2, c1, c2 = pos[0] - 1, pos[0] + 1, pos[1] - 1, pos[1] + 1
    else:
        if pos[2]:
            r1, r2, c1, c2 = pos[0] - 1, pos[0] + 1, pos[1], pos[1]
        else:
            r1, r2, c1, c2 = pos[0], pos[0], pos[1] - 1, pos[1] + 1

    if r1 < 0 or c1 < 0 or r2 >= n or c2 >= n: return False
    if visit[pos[0]][pos[1]][pos[2]]: return False
    
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if arr[r][c]: return False
    return True

pos_s, pos_e = init(n, arr)

def bfs(n, arr, pos_s, pos_e):
    res = 0
    q = deque()
    q.append(pos_s)
    visit = [[[False, False] for _ in range(n)] for _ in range(n)]
    visit[pos_s[0]][pos_s[1]][pos_s[2]] = True

    while q:
        size = len(q)
        for _ in range(size):
            r, c, d = q.popleft()
            if (r, c, d) == pos_e: return res
            for dr, dc, dd in dir:
                nr = r + dr
                nc = c + dc
                nd = d ^ dd
                np = (nr, nc, nd)

                if not check(arr, visit, np, dd): continue
                
                visit[nr][nc][nd] = True
                q.append(np)
        res += 1
    return 0

print(bfs(n, arr, pos_s, pos_e))