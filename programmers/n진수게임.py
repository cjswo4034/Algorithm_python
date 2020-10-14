etc = '0123456789ABCDEF'

def solution(n, t, m, p):
    nth, value = '0', 1
    while len(nth) < t * m:
        nth += decimal_to_nth(value, n)
        value += 1
    return nth[p - 1::m][:t]

def decimal_to_nth(v, n):
    res = ''
    while v:
        v, r = divmod(v, n)
        res = etc[r] + res
    return res

def decimal_to_nth2(v, n):
    q, r = divmod(v, n)
    return decimal_to_nth(q, n) + etc[r] if q else etc[r]

print(str(bin(3))[5:], '123123')