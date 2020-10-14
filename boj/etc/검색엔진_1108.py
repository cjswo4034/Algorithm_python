from collections import defaultdict

import sys

input = sys.stdin.readline

n = int(input())
m = dict()
adj = defaultdict(list)
re_adj = defaultdict(list)
for i in range(n):
    args = input().split()
    if args[0] not in m: m[args[0]] = len(m)
    s = m[args[0]]
    for j in range(int(args[1])):
        jj = 2 + j
        if args[jj] not in m: m[args[jj]] = len(m)
        adj[s].append(m[args[jj]])

target = m[input().replace('\n', '')]

cnt, SN = 0, 0
s = []
sn = [0] * len(m)
dfsn = [0] * len(m)
finished = [False] * len(m)

def dfs(curr):
    global cnt, SN
    
    cnt += 1
    dfsn[curr] = cnt
    s.append(curr)

    res = dfsn[curr]
    for next in adj[curr]:
        if dfsn[next] == 0: res = min(res, dfs(next))
        elif not finished[next]: res = min(res, dfsn[next])
    
    if res == dfsn[curr]:
        while s:
            t = s.pop()
            finished[t] = True
            sn[t] = SN
            if t == curr: break
        SN += 1
        
    return res

for i in range(len(m)):
    if dfsn[i] == 0: dfs(i)
    
score = defaultdict(lambda:1)
indegree = [0] * len(m)

for s in adj:
    for e in adj[s]:
        if sn[s] == sn[e]: continue
        indegree[s] += 1
        re_adj[e].append(s)

q = []
for i in range(len(m)): 
    if indegree[i] == 0: q.append(i)

while q:
    current = q.pop(0)
    for next in re_adj[current]:
        if sn[current] is not sn[next]: 
            score[next] += score[current] 
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

print(score[target])