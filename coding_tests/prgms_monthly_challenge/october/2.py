import sys

sys.setrecursionlimit(10 ** 8)


def solution(arr):
    return function1(arr, [0, 0], [len(arr)] * 2)


def function1(arr, s, e):
    if s[0] + 1 == e[0] or s[1] + 1  == e[1]:
        v = arr[s[0]][s[1]]
        return [1, 0] if v == 0 else [0, 1]

    r1, c1 = s
    r2, c2 = e
    nr, nc = (r1 + r2) // 2, (c1 + c2) // 2
    res_m = function1(arr, [r1, c1], [nr, nc])
    res_d = function1(arr, [nr, c1], [r2, nc])
    res_r = function1(arr, [r1, nc], [nr, c2])
    res_c = function1(arr, [nr, nc], [r2, c2])

    if res_m == res_d == res_r == res_c and (res_m[0] == 1 or res_m[1] == 1): return res_m
    else:
        res = [sum(e) for e in zip(res_m, res_d, res_r, res_c)]
        return res


def function2(arr, s, e):
    if s[0] >= e[0] or s[1] >= e[1]: return [0, 0]

    [r1, c1], [r2, c2] = s, e
    nr, nc = (r1 + r2) >> 1, (c1 + c2) >> 1

    lu = equals(arr, [r1, c1], [nr, nc])
    if not lu: lu = function2(arr, [r1, c1], [nr, nc])
    else:
        if arr[r1][c1]: lu = [0, 1]
        else: lu = [1, 0]

    ld = equals(arr, [nr, c1], [r2, nc])
    if not ld: ld = function2(arr, [nr, c1], [r2, nc])
    else:
        if arr[nr][c1]: ld = [0, 1]
        else: ld = [1, 0]

    ru = equals(arr, [r1, nc], [nr, c2])
    if not ru:ru = function2(arr, [r1, nc], [nr, c2])
    else:
        if arr[r1][nc]: ru = [0, 1]
        else: ru = [1, 0]

    rd = equals(arr, [nr, nc], [r2, c2])
    if not rd: rd = function2(arr, [nr, nc], [r2, c2])
    else:
        if arr[nr][nc]: rd = [0, 1]
        else: rd = [1, 0]

    if lu == ld == ru == rd and (sum(lu) == 1): return lu
    return [sum(e) for e in zip(lu, ld, ru, rd)]


def equals(arr, s, e):
    res = arr[s[0]][s[1]]
    for r in range(s[0], e[0]):
        for c in range(s[1], e[1]):
            if arr[r][c] != res: return False
    return True


arr1 = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr1))

print((30 + 32) // 2)