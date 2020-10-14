# 1. 트리로 맵을 만든다.
# 2. dfs로 각각의 뎁스마다 움직일 주사위를 선택한다.

ans, END_POINT = 0, 32
points = list(range(0, 41, 2)) + list(range(13, 23, 3)) + [24, 28, 27, 26, 25, 30, 35, 0]
edges = {i:i + 1 for i in range(20)}
edges.update({i:i + 1 for i in [21, 22, 24, 26, 27, 28, 29, 30]})
edges.update({s:e for s, e in [[31, 20], [20, 32], [23, 29], [25, 29]]})
blue_edge = {5:21, 10:24, 15:26}

visit = set()
dice_pos = [[0], [0], [0], [0]]
dice = list(map(int, input().split()))

def dfs(turn, point):
    if turn == 10: 
        global ans
        ans = max(ans, point)
        return
    
    tmp = tuple(map(tuple, sorted(dice_pos)))
    if tmp in visit: return
    visit.add(tmp)
    
    for i in range(min(turn + 1, 4)):
        curr_pos = dice_pos[i][-1]

        if curr_pos == END_POINT: continue
        
        # 주사위의 현재 위치가 파란칸이면 샛길로 이동
        if curr_pos in blue_edge: next_pos = move(blue_edge[curr_pos], dice[turn] - 1)
        else: next_pos = move(curr_pos, dice[turn])

        # 주사위가 도착할 위치에 말이 있다면 이동 불가
        if next_pos != END_POINT and next_pos in [dp[-1] for dp in dice_pos]: continue
        
        dice_pos[i].append(next_pos)
        dfs(turn + 1, point + points[next_pos])
        dice_pos[i].pop()
 
# 이동할 칸의 위치를 반환
def move(pos, count):
    # 도착칸이 나오면 남은 count에 관계없이 리턴
    for i in range(count):
        if pos == END_POINT: break
        pos = edges[pos]
    return pos

dfs(0, 0)
print(ans)