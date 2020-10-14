def solution(key, lock):
    # a. lock == 1 : return true
    # b. key == 0 : return false
    if check(lock, len(lock) * len(lock[0])):
        return True
    if check(key, 0):
        return False

    # 1. split Arr
    # 2. key is able to contain lock
    # 3. merge key and lock
    # 4. rotate Arr

    key = split(key, 1)
    lock = split(lock, 0)

    printArr(key)
    printArr(lock, False)

    for _ in range(4):
        if not isIn(key, lock): continue
        if isOpenable(key, lock): return True
        lock = rotate(lock)

    return False

def printArr(arr, isKey = True):
    print('-------------- ', 'key' if isKey else 'lock')
    for r in arr:
        line = ""
        for c in r:
            line += str(c) + " "
        print(line)

def split(arr, value):
    minR, minC = len(arr), len(arr[0])
    maxR, maxC = 0, 0

    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == value:
                minR, minC = min(minR, r), min(minC, c)
                maxR, maxC = max(maxR, r), max(maxC, c)

    return [[el for el in row[minC:maxC + 1]] for row in arr[minR:maxR + 1]]

def isIn(key, lock):
    return len(key) >= len(lock) and len(key[0]) >= len(lock[0])

def rotate(arr):
    row, col = len(arr), len(arr[0])
    return [[arr[row - c - 1][r] for c in range(row)] for r in range(col)]

def isOpenable(key, lock):
    tot = len(lock) * len(lock[0])
    row, col = len(lock), len(lock[0])
    rTo, cTo = len(key) - len(lock), len(key[0]) - len(lock[0])

    for r in range(rTo + 1):
        for c in range(cTo + 1):
            arr = [[key[r + _r][c + _c] ^ lock[_r][_c] for _c in range(col)] for _r in range(row)]
            if check(arr, tot):
                return True
    return False

def check(arr, value):
    return sum(sum(arr, [])) == value


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))