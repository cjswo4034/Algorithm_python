def solution(n, build_frame):
    answer = []
    frame = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    pilar = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # col, row, {0: p, 1:f}, {0: remove, 1: build}
    for col, row, type, cmd in build_frame:
        row = n - row
        # 구조물을 설치한다.
        if type: frame[row][col] = cmd
        else: pilar[row][col] = cmd

        # 설치한 구조물을 검증한다.
        if not buildable(frame, pilar):
            if type: frame[row][col] = cmd ^ 1
            else: pilar[row][col] = cmd ^ 1
    
    for col in range(n + 1):
        for row in range(n, -1, -1):
            if pilar[row][col]:
                answer.append([col, n - row, 0])
            if frame[row][col]:
                answer.append([col, n - row, 1])
    return answer

def buildable(frame, pilar):
    for row in range(len(frame)):
        for col in range(len(pilar)):
            if frame[row][col] and not verify_frame(frame, pilar, row, col):
                return False
            if pilar[row][col] and not verify_pilar(frame, pilar, row, col):
                return False
    return True

# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다
def verify_pilar(frame, pilar, row, col):
    # 바닥 위에 있거나
    if row == len(frame) - 1: return True

    # 보의 한쪽 끝 부분 위에 있거나 (오)
    if frame[row][col] or (col - 0 >= 0 and frame[row][col - 1]):
        return True

    # 다른 기둥 위에 있어야 한다.
    if row + 1 < len(pilar) and pilar[row + 1][col]:
        return True
    return False

# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
def verify_frame(frame, pilar, row, col):
    # 한쪽 끝 부분이 기둥 위에 있다.
    if row + 1 < len(pilar) and (pilar[row + 1][col] or \
        (col + 1 < len(pilar) and pilar[row + 1][col + 1])):
        return True
    # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 한다.
    if (col - 1 >= 0 and frame[row][col - 1]) and (col + 1 < len(frame) and frame[row][col + 1]):
        return True
    return False

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))