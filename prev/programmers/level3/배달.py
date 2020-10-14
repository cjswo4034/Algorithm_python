import heapq as hq

def solution(N, roads, K):
    arr = [[] for _ in range(N + 1)]
    for road in roads:
        arr[road[0]].append([road[1], road[2]])
        arr[road[1]].append([road[0], road[2]])
    pq = []
    dist = [123456789] * (N + 1)
    visit = [False] * (N + 1)
    print(arr)
    dist[1] = 0
    hq.heappush(pq, [0, 1])
    while pq:
        curr = hq.heappop(pq)[1]
        while pq and visit[curr]:
            curr = hq.heappop(pq)[1]
        if visit[curr]: break
        visit[curr] = True

        for el in arr[curr]:
            next, d = el[0], el[1]
            if dist[next] > dist[curr] + d:
                dist[next] = dist[curr] + d
                hq.heappush(pq, [dist[next], next])

    return sum([1 for d in dist if d <= K])


print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))
