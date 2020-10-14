import sys

input = sys.stdin.readline

s = input().replace("\n", '')

def solution_rabin_karp(s):
    power = 1
    def update_hash(remove, add, hash):
        return 31 * (hash - remove * power + add)

    def rabinkarp(src, length):
        s = set()
        start, power = 0, 1
        for _ in range(length): power *= 31
        for i in range(length): start = update_hash(0, ord(src[i]), start)
        s.add(start)
        for i in range(length, len(src)):
            start = update_hash(ord(src[i - length]), ord(src[i]), start)
            if start in s: return True
            s.add(start)
        return False

    res = 0
    l, r = 0, len(s) - 1
    while l <= r:
        m = (l + r) >> 1
        if rabinkarp(s, m):
            l = m + 1
            res = max(res, m)
        else: r = m - 1

    return res


def solution_kmp(s):
    def get_pi(src):
        res = 0
        pi, j = [0] * len(src), 0
        for i in range(1, len(src)):
            while j > 0 and src[i] != src[j]: j = pi[j - 1]
            if src[i] == src[j]:
                j += 1
                pi[i] = j
                res = max(res, j)
        return res

    def kmp(s):
        res, pi = 0, [0] * len(s)
        begin, matched = 1, 0
        while begin + matched < len(s):
            if s[begin + matched] == s[matched]:
                matched += 1
                pi[begin + matched - 1] = matched
                res = max(res, matched)
            else:
                if matched == 0: begin += 1
                else:
                    begin += matched - pi[matched - 1]
                    matched = pi[matched - 1]
        return res

    ans = 0
    for i in range(len(s)):
        if len(s) - i < ans: break
        ans = max(ans, kmp(s[i:]))
        # ans = max(ans, get_pi(s[i:]))

    return ans

print('kmp ', solution_kmp(s))
print('rabin ', solution_rabin_karp(s))