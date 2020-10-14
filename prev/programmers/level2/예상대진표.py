def solution(n,a,b):
    answer = get_exp(n)
    l, r = 1, n
    while l < r:
        m = (l + r) // 2
        if a <= m and b <= m: r = m
        elif a > m and b > m: l = m + 1
        else: return answer
        answer -= 1
    return answer


def get_exp(n):
    res = 0
    while n > 1:
        n >>= 1
        res += 1
    return res


print(solution(8, 4, 7))
