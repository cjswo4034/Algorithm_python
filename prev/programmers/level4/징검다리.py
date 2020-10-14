def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    l, r = 0, distance
    while l < r:
        mid = (l + r + 1) // 2
        p, hits = 0, 0
        for rock in rocks:
            if rock - p < mid: hits += 1
            else: p = rock
        if hits > n: r = mid - 1
        else: l = mid
    return l


print(solution(25, [2, 14, 11, 21, 17], 2))