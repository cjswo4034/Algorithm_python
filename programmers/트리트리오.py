""" ******** Python은 실패, Java는 통과 ********
[Level 4]
f(a, b)를 정점 a와 b 사이의 간선의 개수라고 할 때,
n개의 점으로 이루어진 트리에서 f(a, b), f(a, c), f(b, c)의 평균이 최대인 거리를 구한다.
 - 트리에서 지름이 가장 긴 두 정점 a, b를 구한다.
 - 두 정점을 제외한 나머지 정점들을 순회하면서 평균값이 최대인 거리를 구한다.
"""
from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10 ** 9)


def solution(n, edges):
    visit = [False] * (n + 1)
    adj = defaultdict(list)
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    # 1. 트리에서 지름이 가장 긴 두 정점 a, b를 구한다.
    # a: [idx, 0], b: [idx, diameter]
    a, b = get_two_end_vertices(adj, visit)

    # 2. a와 b에서 나머지 정점까지의 거리를 구한다.
    a_dist = [0] * (n + 1)  # a -> c
    b_dist = [0] * (n + 1)  # b -> c

    set_distances_bfs(adj, a_dist, a)
    set_distances_bfs(adj, b_dist, b)
    a_dist[a] = b_dist[a] = b_dist[b] = 0

    # 3. a-b, a-c, b-c 거리의 합이 가장 큰 거리를 구한다.
    answer = (0, 0)
    for i in range(1, n + 1):
        if i is not b and sum(answer) < a_dist[i] + b_dist[i]:  # a -> b, a -> c, b -> c
            answer = (a_dist[i], b_dist[i])

    return min(max(answer), a_dist[b])


def set_distances_bfs(adj, dist, root):
    q = deque()
    q.append(root)

    dist[root] = -1
    distance = 1
    while q:
        for _ in range(len(q)):
            v = q.popleft()
            for nv in adj[v]:
                if dist[nv]: continue

                dist[nv] = distance
                q.append(nv)

        distance += 1


def set_distances_dfs(adj, dist, root, distance):
    if dist[root]: return
    dist[root] = distance

    for nv in adj[root]:
        set_distances_dfs(adj, dist, nv, distance + 1)


# 지름이 가장 길 때 양 끝 정점을 구한다.
def get_two_end_vertices(adj, visit):
    a, b = [1, 0], [1, 0]
    get_farthest_vertex(adj, visit, 1, 0, a)     # 정점 1에서 가장 먼 정점 2

    for i in range(len(visit)): visit[i] = False
    get_farthest_vertex(adj, visit, a[0], 0, a)  # 정점 2에서 가장 먼 정점 A

    for i in range(len(visit)): visit[i] = False
    get_farthest_vertex(adj, visit, a[0], 0, b)  # 정점 A에서 가장 먼 정점 B

    return a[0], b[0]


# args: [vertex, distance]
def get_farthest_vertex(adj, visit, root, weight, args):
    if visit[root]: return
    visit[root] = True

    if weight > args[1]:
        args[0] = root
        args[1] = weight

    for nv in adj[root]:
        get_farthest_vertex(adj, visit, nv, weight + 1, args)


print(solution(4, [[1, 2], [2, 3], [3, 4]]))
