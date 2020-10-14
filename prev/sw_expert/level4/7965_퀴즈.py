#  I^I -> I^(I/2)*I^(I/2)
# len = 0
# while cnt >= (2 << (len + 1)):
#     len += 1


def solution(num, cnt, arr):
    if cnt <= 4:
        arr[cnt] = pow(num, cnt)
    if arr[cnt]:
        return arr[cnt]

    half_cnt = int(cnt / 2)
    if cnt % 2 == 0:
        return (solution(num, half_cnt, arr) * solution(num, half_cnt, arr)) % 1000000007
    else:
        return (solution(num, half_cnt, arr) * solution(num, half_cnt + 1, arr)) % 1000000007


T = int(input())

for case in range(1, T + 1):
    n, ans = int(input()), 0
    for i in range(1, n + 1):
        mem = [0 for _ in range(i + 1)]
        ans = (ans + solution(i, i, mem)) % 1000000007

    print(f'#{case} {ans}')
