import sys
# n, m = map(int, input().split())
# arr = list(map(int, sys.stdin.readline().split()))
n, m = map(int, "2 15".split())
arr = list(map(int, "3 2 1 2 1 2 1 2 1 3 3 3 3 3 3".split()))

# 최적 페이지 교체 알고리즘. 가장 먼 곳에 있는 플러그를 뺀다.
def solution(n, m, arr):
    if n >= m: return 0
    answer = 0
    cache = []
    for i in range(m):
        if arr[i] in cache: continue
        if len(cache) < n:
            cache.append(arr[i])
            continue
        
        max_idx, idx = 0, 0
        for j in range(n):
            try:
                tmp = arr.index(cache[j], i + 1)
                if max_idx < tmp:
                    max_idx = tmp
                    idx = j
            except ValueError:
                idx = j
                break
        
        cache[idx] = arr[i]
        answer += 1
    return answer

print(solution(n, m, arr))