import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [(*map(int, input().split()), i) for i in range(n)]
arr_1 = sorted([(e[0], e[3]) for e in arr])
arr_2 = sorted([(e[1], e[3]) for e in arr])
arr_3 = sorted([(e[2], e[3]) for e in arr])

q = []
for i in range(n - 1):
    heapq.heappush(q, (abs(arr_1[i][0] - arr_1[i + 1][0]), arr_1[i][1], arr_1[i + 1][1]))
    heapq.heappush(q, (abs(arr_2[i][0] - arr_2[i + 1][0]), arr_2[i][1], arr_2[i + 1][1]))
    heapq.heappush(q, (abs(arr_3[i][0] - arr_3[i + 1][0]), arr_3[i][1], arr_3[i + 1][1]))

union = [-1] * n

def find(i):
    if union[i] == -1: return i
    union[i] = find(union[i])
    return union[i]

def merge(i, j):
    i = find(i)
    j = find(j)
    if i == j: return False
    union[i] = j
    return True

answer = 0
cnt = n - 1
while cnt > 0:
    curr = heapq.heappop(q)
    
    if merge(curr[1], curr[2]):
        answer += curr[0]
        cnt -= 1
        
print(answer)