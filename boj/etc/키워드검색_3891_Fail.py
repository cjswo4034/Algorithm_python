import sys
 
# 시간초과
def check(depth, visit, arr, sub_str):
    if depth == len(arr): return sub_str.strip() == ''
    
    for i in range(len(arr)):
        if visit[i] or arr[i] not in sub_str: continue
        visit[i] = True
        next_str = sub_str.replace(arr[i], ' ', 1)
        if check(depth + 1, visit, arr, next_str): return True
        visit[i] = False
    return False

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if n == m == 0: break

    ans = 0
    arr = [input().replace('\n', '') for _ in range(n)]
    s = ''.join([input().replace('\n', '') for _ in range(m)])
    length = sum(map(len, arr))

    for i in range(0, len(s) - length + 1):
        if check(0, [False] * len(arr), arr, s[i:i+length]): ans += 1

    print(ans)