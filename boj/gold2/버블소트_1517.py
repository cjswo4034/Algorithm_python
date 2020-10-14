import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

def merge_sort(arr):
    if len(arr) <= 1: return 0
    res = 0
    
    l = len(arr)
    left = arr[:l // 2]
    right = arr[l // 2:]

    res += merge_sort(left)
    res += merge_sort(right)

    res += merge(arr, left, right)

    return res

def merge(arr, arr_l, arr_r):
    ls, rs = 0, 0
    res, pos = 0, 0
    
    while ls < len(arr_l) and rs < len(arr_r):
        if arr_l[ls] <= arr_r[rs]:  # 같은 숫자 나올 때 개수 셀 필요없음
            arr[pos] = arr_l[ls]
            ls += 1
        else:
            arr[pos] = arr_r[rs]
            res += len(arr_l) - ls
            rs += 1
        pos += 1
    
    while ls < len(arr_l):
        arr[pos] = arr_l[ls]
        pos += 1
        ls += 1
    
    while rs < len(arr_r):
        arr[pos] = arr_r[rs]
        pos += 1
        rs += 1

    return res

print(merge_sort(arr))