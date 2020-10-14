from functools import cmp_to_key

def get_sa(s):
    t, n = 1, len(s)
    sa = [0] * n
    tg = [0] * n
    g = [0] * n

    def comp(x, y):
        if g[x] == g[y]: # 그룹이 같으면
            l = g[x + t] if x + t < len(g) else 0
            r = g[y + t] if y + t < len(g) else 0
            if l == r: return 0
            return -1 if l < r else 1
        return -1 if g[x] < g[y] else 1

    for i in range(n):  # 첫 글자를 기준으로 그룹 배정
        sa[i] = i
        g[i] = ord(s[i]) - ord('a')
    
    while t <= n:
        sa = sorted(sa, key=cmp_to_key(comp))
        tg[sa[0]] = 0
        for i in range(1, n):   # 다음 그룹 배정
            tg[sa[i]] = tg[sa[i - 1]] + (1 if comp(sa[i - 1], sa[i]) else 0)    # 다르면 다른 그룹
        g = tg
        t <<= 1
    return sa

def lcp(s, sa):
    n, length = len(s), 0
    lcp = [0] * n
    rank = [0] * n  # i번째 배열이 사전순으로 몇 번째 접미사인가?
    for i in range(n): rank[sa[i]] = i
    
    for i in range(n):
        k = rank[i]         # 검사할 접미사
        if k:
            j = sa[k - 1]   # 정렬된 접미사 배열에서 검사할 접미사의 바로 이전 접미사
            while i + length < len(s) and j + length < len(s) and s[j + length] == s[i + length]: length += 1

            lcp[k] = length

            if length: length -= 1

    return lcp

sa = get_sa('banana')
print('[Suffix]')
for i in sa: print('banana'[i:])

print('\n[Suffix Order]')
for i in sa: print(i + 1)

print('\n[LCP]')
print(lcp('banana', sa))