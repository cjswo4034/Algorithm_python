def solution(n, times):
    l = 1
    r = max(times) * n
    print(l, r)
    ans = r
    while l <= r:
        m = int((l + r) / 2)
        tot = sum([int(m / time) for time in times])

        if tot < n:
            l = m + 1
        else:
            ans = min(m, ans)
            r = m - 1
        print(l, r, m, tot)

    return ans


print(solution(6, [7, 10]))