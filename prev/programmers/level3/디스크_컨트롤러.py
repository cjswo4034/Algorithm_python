def solution(jobs):
    arr = jobs.copy()
    arr.sort(key=lambda x: (x[0], x[1]))

    q = [arr.pop(0)]
    tot, time = 0, q[0][0]

    while q:
        q.sort(key=lambda x: x[1])

        curr = q.pop(0)
        time = max(time + curr[1], sum(curr))
        tot += abs(time - curr[0])

        while arr and arr[0][0] <= time:
            q.append(arr.pop(0))

        if arr and not q:
            q.append(arr.pop(0))
            time = max(time, q[0][0])

    return int(tot / len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[1, 9]]))
