# r값 수정 후
# 효율성 전부 시간초과
# 정확성 다 맞음
def solution(lands, P, Q):
    lands, ans = sum(lands, []), 0
    l, r, v = 0, max(lands) * max(P, Q) * len(lands), 0
    while l <= r:
        m, v = (l + r) >> 1, 0
        a, b, c = 0, 0, 0  # m + 1 층, m 층, m - 1층
        for land in lands:
            if land < m:
                v = v + (m - land) * P
                c += 1
            elif land > m:
                v = v + (land - m) * Q
                a += 1
            else: b += 1

        p = v - a * Q + (b + c) * P     # m + 1층: a * - Q + (b + c) * P -> len(lends) - a * P
        pp = v - c * P + (a + b) * Q    # m - 1층: c * - P + (a + b) * Q

        # print(f'{m + 1}층: {p}, {m}층: {v}, {m - 1}층: {pp}, ({a}, {b}, {c})')

        if p > v > pp: r = m - 1
        elif p < v < pp: l = m + 1
        else:
            ans = m
            break
    return calculate(lands, P, Q, ans)


# 막 풀기
# min(land) ~ max(land)를 순회하면서 i보다 크면 (land - i) * q, 작으면 (i - land) * p를 더한 값의 최솟값
# 개선: min ~ max 까지 탐색하는게 오래걸림 (각 블록당 범위: 0 ~ 10억)
# 개선: 한 층을 이동할 때 처음부터 계산할 필요 없음.
#       i 층에서 -> i + 1: (i층에 있는 블록 * p - i층의 빈 블록 * q). i - 1: 반대로.
def solution1(land, P, Q):
    land = sum(land, [])
    answer = 987654321987654
    for i in range(min(land), max(land) + 1):
        answer = min(answer, calculate(land, P, Q, i))
    return answer


# 자바에서 통과
def solution2(lands, P, Q):
    lands, ans = sum(lands, []), 0
    length = len(lands)
    l, r, v = min(lands), max(lands), 0
    while l <= r:
        m, v = (l + r) >> 1, 0
        a, b = 0, 0     # m + 1 블럭, m - 1 블럭의 개수
        for land in lands:
            if land < m:
                v = v + (m - land) * P
                b += 1
            elif land > m:
                v = v + (land - m) * Q
                a += 1

        p = v - a * Q + (length - a) * P     # m + 1층: a * - Q + (len(lends) - a) * P
        pp = v - b * P + (length - b) * Q    # m - 1층: b * - P + (len(lands) - b) * Q

        if p > v > pp: r = m - 1
        elif p < v < pp: l = m + 1
        else: return v


def solution3(lands, P, Q):
    lands = sorted(sum(lands, []))
    answer, length = 0, len(lands)
    accumulated_blocks, total_blocks = 0, sum(lands)
    for i, l in enumerate(lands):
        accumulated_blocks += l
        adder = l * (i + 1) - accumulated_blocks
        deleter = (total_blocks - accumulated_blocks - (length - i - 1) * l)
        resource = adder * P + deleter * Q
        answer = min(answer, resource)
    return answer


def calculate(land, P, Q, v):
    res = 0
    for l in land:
        if v < l: res += (l - v) * Q
        elif v > l: res += (v - l) * P
    return res


print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))
print(solution1([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))
print(solution3([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))
print("-------------")
print(solution([[1, 2], [2, 3]], 3, 2))
print(solution1([[1, 2], [2, 3]], 3, 2))
print(solution3([[1, 2], [2, 3]], 3, 2))

print([1, 2, 3, 4, 5].count(lambda x: x < 3))