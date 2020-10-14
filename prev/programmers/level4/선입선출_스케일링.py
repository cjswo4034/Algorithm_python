def solution(n, cores):
    answer = -1
    time = 50000*10000
    l, r = min(cores) * n // len(cores), max(cores) * n
    rest = n - len(cores)

    while l <= r:
        mid = (l+r) >> 1
        completedWork = 0
        for c in cores:
            completedWork += mid//c

        if completedWork < rest:
            l = mid+1
        else:
            if time > mid:
                time = mid
            r = mid - 1

    for i in cores:
        rest -= (time - 1) // i

    while rest is not 0:
        answer += 1
        rest -= 1 if time % cores[answer] == 0 else 0

    return answer+1


def solution1(n, cores):  # Parametric Search 효율성 2개 x
    if n <= len(cores): return n;
    l, r = min(cores) * n // len(cores), max(cores) * n
    while l <= r:
        core, cnt = len(cores), 0
        mid = (l + r) >> 1

        for c in cores:
            core += (mid // c)
            if mid % c == 0:
                cnt += 1

        if n > core: l = mid + 1
        elif n <= core - cnt: r = mid - 1;
        else:
            tmp = 0
            for i in range(len(cores)):
                if mid % cores[i] == 0: tmp += 1
                if tmp == n - (core - cnt): return i + 1


def solution2(n, cores):  # 실패
    answer = 0
    arr = [[] for _ in range(max(cores) * n)]
    for core in cores:
        for a in arr[::core]:
            a.append(core)

    for i in range(len(arr)):
        if n - len(arr[i]) <= 0:
            answer = arr[i][n - 1]
            break
        n -= len(arr[i])
    return cores.index(answer) + 1, answer


def solution3(n, cores):  # 효율성 X
    answer, time = 0, 0
    while n > 0:
        for i, core in enumerate(cores):
            if time % core == 0:
                print(n, time, core)
                n -= 1
                if n == 0:
                    answer = i
                    break
        time += 1
    return answer + 1


print(solution(5, [2, 1, 3]))
print(solution(6, [1, 3, 2]))
# 1 : 1 2 3
#