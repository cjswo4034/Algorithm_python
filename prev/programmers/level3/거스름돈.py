def solution(n, money):
    arr = [[0] * len(money) for _ in range(n + 1)]
    arr[0] = [1 for _ in range(len(money))]

    for curr in range(len(money)):
        for remainder in range(1, len(arr)):
            arr[remainder][curr] = arr[remainder - money[curr]][curr] +\
                                   arr[remainder][curr - 1]

    ######################################

    mem = [0] * (n + 1)
    mem[0] = 1
    for coin in money:
        for curr in range(coin, n + 1):
            mem[curr] += mem[curr - coin]

    return arr[n][-1], mem[n]


print(solution(3, [1, 2, 5]))
