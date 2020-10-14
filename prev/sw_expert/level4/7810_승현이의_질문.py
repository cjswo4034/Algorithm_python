T = int(input())


for test_case in range(1, T + 1):
    tot = n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    ans = 0
    for el in arr:
        if tot <= el:
            ans = max(ans, tot)
        tot -= 1

    print(f'#{test_case} {ans}')
