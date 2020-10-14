T = int(input())
union = []


def find(a):
    if union[a] == -1: return a;
    union[a] = find(union[a])
    return union[a]


def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    union[b] = a
    return False


for test_case in range(1, T + 1):
    ans = ''
    n, m = map(int, input().split())
    union = [-1] * (n + 1)

    for _ in range(m):
        a, b, c = map(int, input().split())
        if not a:
            merge(b, c)
        else:
            if find(b) == find(c):
                ans += '1'
            else:
                ans += '0'

    print(f'#{test_case} {ans}')
