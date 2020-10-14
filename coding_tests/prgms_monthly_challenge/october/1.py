def solution(n):
    answer = to_3th(n)[::-1]
    return to_decimal(answer)

def to_3th(n):
    res = ''
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res

def to_decimal(n):
    res = 0
    for i in range(len(n)):
        res += (3 ** i) * (int(n[i]))
    return res


print(to_3th(45)[::-1])
print(to_decimal(to_3th(45)))