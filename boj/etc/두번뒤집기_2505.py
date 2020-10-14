# P4
import sys

input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
sorted_arr = sorted(arr)

def find(arr):
    res = []
    for i in range(1, len(arr)):
        if i == arr[i]: continue
        j = i + 1
        while j < len(arr) and arr[j] != i: j += 1
        arr = arr[:i] + list(reversed(arr[i:j + 1])) + arr[j + 1:]
        res.append(f'{i} {j}')
        if len(res) == 3: break

    if len(res) == 1: res.append('1 1'); return res
    elif len(res) == 2: return res
    else: return False

def rfind(arr):
    res = []
    for i in range(len(arr) - 1, 0, -1):
        if i == arr[i]: continue
        j = i - 1
        while j > 0 and arr[j] != i: j -= 1
        arr = arr[:j] + list(reversed(arr[j:i + 1])) + arr[i + 1:]
        res.append(f'{j} {i}')
        if len(res) == 2: break

    if len(res) == 1: res.append('1 1'); return res
    elif len(res) == 2: return res
    else: return False

if arr == sorted_arr: ans = ['1 1', '1 1']
else:
    ans = find(arr)
    if not ans: ans = rfind(arr)
print('\n'.join(ans))