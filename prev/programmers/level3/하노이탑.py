def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer


def hanoi(n, f, mid, to, ans):
    if n == 0: return
    hanoi(n - 1, f, to, mid, ans)
    ans.append([f, to])
    hanoi(n - 1, mid, f, to, ans)


def hanoi2(n):
    def _hanoi(m, s, b, d):
        if m == 1:
            yield [s, d]
        else:
            yield from _hanoi(m-1, s, d, b)
            yield [s, d]
            yield from _hanoi(m-1, b, s, d)

    ans = list(_hanoi(n, 1, 2, 3))
    return ans

print(solution(3))