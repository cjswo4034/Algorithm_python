import sys
sys.setrecursionlimit(10000)

def solution(s):
    return min(len(compress(s, 1, n)) for n in range(1, len(s) // 2 + 2))

def compress(s, cnt, n):
    if len(s) < n: return s
    prev = s[:n]
    post = s[n:]

    if not post.startswith(prev):
        if cnt == 1: return prev + compress(post, 1, n)
        return str(cnt) + prev + compress(post, 1, n)

    return compress(post, cnt + 1, n)

print(solution('a'))