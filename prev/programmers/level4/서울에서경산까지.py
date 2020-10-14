def solution(K, travel):
    dp = [[0 for _ in range(K + 1)] for _ in range(len(travel))]
    dp[0][travel[0][0]] = travel[0][1]
    dp[0][travel[0][2]] = travel[0][3]

    prev = max(travel[0][0::2])
    for i in range(1, len(travel)):
        r_time, r_fare, c_time, c_fare = travel[i]
        limit = max(travel[i][0::2]) + prev
        limit = min(limit, K)
        for j in range(limit + 1):
            if j - r_time >= 0 and dp[i - 1][j - r_time]: dp[i][j] = max(dp[i][j], dp[i - 1][j - r_time] + r_fare)
            if j - c_time >= 0 and dp[i - 1][j - c_time]: dp[i][j] = max(dp[i][j], dp[i - 1][j - c_time] + c_fare)
        prev = limit
    return max(dp[len(travel) - 1])


print(solution(1650, [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]))