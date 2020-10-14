def solution(n):
    a, b = 1, 1  # 0번째, 1번쨰
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


print(solution(4))