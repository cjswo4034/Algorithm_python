from collections import Counter
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
l, r = arr[:n//2], arr[n//2:]
a, b = [0], [0]

def extend(o, l):
    for i in l:
        tmp = [j + i for j in o]
        o += tmp

extend(a, l)
extend(b, r)

c = Counter(b)

ans = 0 if k else -1
for i in a:
    if k - i in c:
        ans += c[k - i]
print(ans)