# 1. 명령대로 설치한다.
# 2. 구조물이 규칙에 맞는지 확인한다.
# 3. 규칙에 어긋나면 명령 이전상태로 되돌린다.

def solution(n, build_frame):
    answer = []
    pillar = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    frame = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for [c, r, is_frame, build] in build_frame:
        # 1. 구조물 설치
        if is_frame: frame[r][c] = build
        else: pillar[r][c] = build

        # 2. 모순 확인
        if not validation(frame, pillar, r, c):
            if is_frame: frame[r][c] ^= 1
            else: pillar[r][c] ^= 1

    for r in range(n + 1):
        for c in range(n + 1):
            if pillar[r][c]: answer.append([c, r, 0])
            if frame[r][c]: answer.append([c, r, 1])
    return sorted(answer)


def validation(frame, pillar, row, col):
    n = len(frame)
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            r = row + dr
            c = col + dc
            if r < 0 or c < 0 or r >= n or c >= n: continue
            if frame[r][c] and not validate_frame(frame, pillar, r, c): return False
            if pillar[r][c] and not validate_pillar(frame, pillar, r, c): return False
    return True


def validate_pillar(frame, pillar, r, c):
    # 기둥은 바닥 위에 있어야 한다
    if r == 0: return True
    # 다른 기둥 위에 있어야 한다
    if pillar[r - 1][c]: return True
    # 보의 한쪽 끝 부분 위에 있어야 한다
    if frame[r][c] or (c > 0 and frame[r][c - 1]): return True
    return False


def validate_frame(frame, pillar, r, c):
    # 보는 한쪽 끝 부분이 기둥 위에 있거나 (왼쪽, 오른쪽)
    if r > 0 and pillar[r - 1][c]: return True
    if r > 0 and c + 1 < len(frame) and pillar[r - 1][c + 1]: return True
    # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 한다.
    if 0 < c < len(frame) - 1 and frame[r][c - 1] and frame[r][c + 1]: return True
    return False


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))