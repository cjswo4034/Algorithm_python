from itertools import permutations


def solution(n, weak, dist):
    res = len(dist) + 1
    weaks = [get_weak(weak, i, n) for i in range(len(weak))]
    for weak in weaks:
        for i in range(1, len(dist) + 1):
            if i >= res: break
            for perm in permutations(dist, i):  # TODO 길이가 len(dist)인 조합을 검사. (모든 외관 검사 가능하면 길이 리턴)
                if possible_check(perm, weak):
                    res = min(res, i)
    return res if res <= len(dist) else -1


def possible_check(perm, weak):
    possible_length, idx = 0, 0
    for i in range(len(perm)):
        possible_length = weak[idx] + perm[i]
        while idx < len(weak) and possible_length >= weak[idx]:
            idx += 1
        if idx >= len(weak): return True
    if idx < len(weak): return False
    return possible_length >= weak[-1]


def get_weak(weak, to, n):
    res = weak[to:]
    for i in range(to):
        res.append(weak[i] + n)
    return res


print(solution(50, [1], [6]))
