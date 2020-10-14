def solution(n, t, m, p):
    mem = get_numeral_arr(n, t * m)
    return ''.join(mem[p-1::m][:t])


def get_numeral_arr(base, limit):
    notation = '0123456789ABCDEF'
    arr, num = ['0'], 1
    while len(arr) <= limit:
        arr.extend(convert_n(num, base, notation))
        num += 1
    return arr


def convert_n(number, base, notation):
    res = ''
    while number:
        q, r = divmod(number, base)
        res = notation[r] + res
        number = q
    return res


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
