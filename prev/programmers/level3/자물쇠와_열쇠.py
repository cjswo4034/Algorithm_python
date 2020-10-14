# 1. Key로 Lock을 해제할 수 있는지 확인 (Max(Key) >= Max(Lock) and Min(Key) >= Min(Lock)
# 2. Key의 부분 배열 중 최상단의 좌 우, 최하단의 좌 우가 1인 배열을 잘라냄
# 3. Lock의 부분 배열 중 최상단의 좌 우, 최하단의 좌 우가 0인 배열을 잘라냄
# 4. 3.을 2.에 대해 슬라이딩 윈도우 알고리즘으로 순회하며 더함
# 5. 4.에서 3.의 모든 원소가 1이 되면 True


def solution(key, lock):
    key_idx = extract_arr(key, 1)
    lock_idx = extract_arr(lock, 0)

    # 2, 3
    key = [[key[i][j]
           for j in range(key_idx[2], key_idx[3] + 1)]
           for i in range(key_idx[0], key_idx[1] + 1)]
    lock = [[lock[i][j]
           for j in range(lock_idx[2], lock_idx[3] + 1)]
           for i in range(lock_idx[0], lock_idx[1] + 1)]

    # lock이 1로 채워졌을 경우 True
    # key가 비었을 경우 False
    if not lock: return True
    if not key: return False

    # 1
    if not enable_solve(key, lock): return False

    # 4
    for _ in range(4):
        if not (len(key) >= len(lock) and len(key[0]) >= len(lock[0])):
            continue
        if slicing_window(key, lock): return True
        lock = rotate(lock)

    return False


# 5
def check_all_one(key, lock, x, y):
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if key[x + i][y + j] + lock[i][j] != 1:
                return False
    return True


def slicing_window(key, lock):
    # key가 lock보다 항상 크다
    for i in range(len(key) - len(lock) + 1):
        for j in range(len(key[0]) - len(lock[0]) + 1):
            if check_all_one(key, lock, i, j):
                return True
    return False


# 오른쪽으로 회전
def rotate(arr):
    ans = [[0] * len(arr) for _ in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            ans[j][len(arr) - i - 1] = arr[i][j]
    return ans


# 1. Key로 Lock을 해제할 수 있는지 확인 (Max(Key) >= Max(Lock) and Min(Key) >= Min(Lock)
def enable_solve(key, lock):
    key_x, key_y = len(key), len(key[0])
    lock_x, lock_y = len(lock), len(lock[0])
    return max(key_x, key_y) >= max(lock_x, lock_y) and\
           min(key_x, key_y) >= min(lock_x, lock_y)


# 입력된 2차원 배열에 대해서 부분배열을 구함
def extract_arr(arr, value):
    x, nx, y, ny = len(arr), 0, len(arr[0]), 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                x, nx = min(x, i), max(nx, i)
                y, ny = min(y, j), max(ny, j)
    return [x, nx, y, ny]  # 위, 아래, 왼쪽, 오른쪽


key = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
lock = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# slicing_window
print(slicing_window(key, lock))
print(solution(key, lock))