import heapq

direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def solution1(land, height):
    N, answer = len(land), 0
    visit_count, max_count = 0, N * N
    
    q = [(0, 0, 0)]
    visit = [[False] * N for _ in range(N)]

    while visit_count < max_count:
        v, r, c = heapq.heappop(q)

        if visit[r][c]: continue
        visit[r][c] = True
        visit_count += 1
        answer += v

        c_height = land[r][c]
        for dr, dc in direction:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if visit[nr][nc]: continue
            
            nv = abs(c_height - land[nr][nc])
            nv = 0 if nv <= height else nv
            heapq.heappush(q, (nv, nr, nc))

    return answer

# 비효율적 -> 영역 나눌 필요 없음, heapq도 굳이
def solution2(land, height):
    answer, color = 0, 0
    area = [[0] * len(land) for _ in range(len(land))]
    # 1. 영역을 나눈다.
    for r in range(len(land)):
        for c in range(len(land)):
            if area[r][c] == 0:
                color += 1
                area[r][c] = color
                set_area(land, height, area, color, [[r, c]])

    edge = []
    # 2. 타 영역으로 가는 모든 사다리를 구한다.
    for r in range(len(land)):
        for c in range(len(land)):
            for d in direction:
                nr = d[0] + r
                nc = d[1] + c
                if nr < 0 or nc < 0 or nr >= len(land) or nc >= len(land): continue
                if area[r][c] != area[nr][nc]:
                    e = [abs(land[r][c] - land[nr][nc]), area[r][c], area[nr][nc]]
                    heapq.heappush(edge, e)
    
    # 3. MST로 minimum cost를 구한다.
    union = [i for i in range(color + 1)]
    edge_count = 0
    while edge_count + 1 != color:
        e = heapq.heappop(edge)
        if not merge(union, e[1], e[2]): continue
        edge_count += 1
        answer += e[0]

    return answer

def find(union, n):
    if union[n] == n: return n
    union[n] = find(union, union[n])
    return union[n]

def merge(union, a, b):
    a = find(union, a)
    b = find(union, b)
    if a == b: return False
    union[b] = a
    return True

def set_area(land, height, area, color, q):
    while q:
        curr = q.pop(0)

        for d in direction:
            nr = d[0] + curr[0]
            nc = d[1] + curr[1]

            if nr < 0 or nc < 0 or nr >= len(land) or nc >= len(land): continue
            if area[nr][nc]: continue
            if abs(land[nr][nc] - land[curr[0]][curr[1]]) > height: continue
            area[nr][nc] = color
            q.append([nr, nc])