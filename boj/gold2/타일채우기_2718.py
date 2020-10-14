import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(x)

"""
dp[i][type] -> i번째 타일이 type 모양일 때 경우의 수
type    0   1   2   3   4   5
        x   x  xx   o   o  xx
        x   x  xx   x  xx   o
        x   o   o   x  xx   o
        x   o   o   o   o  xx

dp = [[0] * 6 for _ in range(10002)]
dp[0] = [1, 2, 0, 1, 0, 0]
for i in range(1, 10002):
    dp[i][0] = dp[i - 2][0] + dp[i - 1][1] // 2 + dp[i - 1][2] + dp[i - 1][5]
               -> dp[i - 2][0] + dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][5]
               -> dp[i - 2][0] + sum(dp[i - 1])
    
    dp[i][1] = dp[i][0] * 2
               -> dp[i - 1][1] == dp[i - 1][0] * 2
    
    dp[i][2] = dp[i - 1][1] + dp[i - 1][2]
               -> dp[i - 1][0] * 2 + dp[i - 1][2]
    
    dp[i][3] = dp[i][0]
               -> dp[i - 1][3] == dp[i - 1][0]
    
    dp[i][4] = dp[i - 1][5]
               -> dp[i - 1][4] == dp[i - 2][5]
    
    dp[i][5] = dp[i - 1][3] + dp[i - 1][4]
               -> dp[i - 1][0] + dp[i - 2][5]
"""


def solution(n):
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = [1, 0, 0]
    for i in range(1, n):
        dp[i][0] = dp[i - 2][0] + sum(dp[i - 1])
        dp[i][1] = dp[i - 1][0] * 2 + dp[i - 1][1]
        dp[i][2] = dp[i - 1][0] + dp[i - 2][2]
    return dp


t = int(input())
n = [int(input()) for _ in range(t)]
dp = solution(max(n) + 1)
print('\n'.join([str(dp[i][0]) for i in n]))
