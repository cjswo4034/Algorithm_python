import sys
import heapq

input = sys.stdin.readline

k, n = map(int, input().split())
arr = list(map(int, input().split()))
pq = arr[:]
heapq.heapify(pq)

for i in range(1, n):
    v = heapq.heappop(pq)
    for e in arr:
        heapq.heappush(pq, v * e)
        if v % e == 0: break

print(heapq.heappop(pq))