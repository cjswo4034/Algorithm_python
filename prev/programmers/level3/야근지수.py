import heapq


def solution(n, works):
    if sum(works) <= n: return 0
    pq = []
    for work in works:
        heapq.heappush(pq, -work)

    for _ in range(n):
        if not pq: break
        value = heapq.heappop(pq) + 1
        if value < 0:
            heapq.heappush(pq, value)

    # works[works.index(max(works))] -= 1

    return get_sum(pq)


def get_sum(arr):
    return sum([el ** 2 for el in arr])


print(solution(4, [4,3,3]))
print(solution(1, [2,1,2]))
print(solution(3, [1, 1]))


# 잔여량을 균등하게 맞춘다.
# PQ