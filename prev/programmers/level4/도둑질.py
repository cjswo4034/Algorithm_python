def solution(money):
    dp1, dp2 = [0] * len(money), [0] * len(money)
    dp1[0:2] = [money[0], money[0]]  # 첫번째 집을 훔친경우
    dp2[0:2] = [0, money[1]]         # 두번째 집부터 훔친경우
    for i in range(2, len(dp1) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
    dp1[-1] = max(dp1[-2], dp1[-3])
    dp2[-1] = max(dp2[-2], dp2[-3] + money[-1])
    return max(dp1[-1], dp2[-1])


def solution2(money):
    ax, ay, az = money[0], money[0], money[0] + money[2]
    bx, by, bz = 0, money[1], max(money[1], money[2])
    for m in money[3:-1]:
        ax, ay, az = ay, az, max(ay, ax) + m
        bx, by, bz = by, bz, max(by, bx) + m
    return max(ax, ay, by, bz)


print(solution([1,2,3,1,5]))