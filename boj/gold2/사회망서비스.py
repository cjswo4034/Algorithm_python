# 1. 루트를 구한다. root = n * n + 1 / 2, root -= v
# 2. 루트가 얼리 어답터 일 때, 아닐 때 중 최소값을 반환한다.
# 상위 노드가 얼리어답터가 아니면 자신은 얼리어답터다
# 상위 노드가 얼리어답터면 자신은 얼리어답터거나 아니다 -> 아닐 때 자식은 무조건 얼리어답터들이어야 한다.

from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x))

n = int(input())
adj = defaultdict(list)

for i in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(x, p):
    c0, c1 = 0, 1
    for n in adj[x]:
        if p == n: continue
        cc0, cc1 = dfs(n, x)
        c1 += min(cc0, cc1)
        c0 += cc1
    return c0, c1

print(min(dfs(1, 0)))

# 시간초과
def dfs2(node, pnum, p):
    res1, res2 = 1, 0
    for next in adj[node]:
        if pnum == next: continue
        res1 += dfs2(next, node, True)
        res2 += dfs2(next, node, False)

    if p: return min(res1, res2)
    return res1

print(dfs2(1, 0, True))
