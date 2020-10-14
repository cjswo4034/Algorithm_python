import sys

input = sys.stdin.readline

a = input().replace('\n', '')
t = input().replace('\n', '')

if len(a) == 1: t = t.replace(a, '')

# TODO
# 개선: find, rfind에서 매번 같은 자리를 찾음 (ex. a: 'a', t: 'bbbaaaa' -> 'bbb'를 찾는다)
def solution(a, t):
    while True:
        idx = t.find(a)     # 같은 자리를 매번 찾음 -> 비효율
        if idx == -1: break
        t = t[:idx] + t[idx + length:]
        idx = t.rfind(a)
        if idx == -1: break
        t = t[:idx] + t[idx + length:]
    return t

def solution2(a, t):
    r_a = a[::-1]
    l, r = [], []
    i, j, length = 0, len(t) - 1, len(a)
    while i <= j:
        while i <= j:
            l.append(t[i])
            i += 1
            if l[-length:] == a:
                l[-length:] = []
                break
        while i <= j:
            r.append(t[j])
            j -= 1
            if r[-length:] == r_a:
                r[-length:] = []
                break

    for rr in r[::-1]:
        l.append(rr)
        if l[-length:] == a:
            l[-length:] = []

    return ''.join(l)

# !!! 합쳐졌을 경우를 고려해야 됨
def solution_kmp(a, t):
    length = len(a)
    def kmp(a):
        pi, j = [0] * len(a), 0
        for i in range(1, len(a)):
            while j > 0 and a[i] != a[j]: j = pi[j - 1]
            if a[i] == a[j]: j += 1
        return pi

    def finds(a, t):
        res = []
        pi, j = kmp(a), 0
        for i in range(len(t)):
            while j > 0 and t[i] != a[j]: j = pi[j - 1]
            if t[i] == a[j]:
                if j == len(a) - 1:
                    res.append(i - len(a) + 1)
                    j = 0
                else: j += 1
        return res

    idx = finds(a, t)
    re_idx = [len(t) - i - len(a) for i in finds(a[::-1], t[::-1])]

    a = list(a)
    t = list(t)
    for i in range(len(idx)):
        s = idx[i]
        e = re_idx[i]
        if s > e: break
        for j in range(len(a)):
            t[s + j] = t[e + j] = ''

    return ''.join(t)

print(solution2(list(a), t))