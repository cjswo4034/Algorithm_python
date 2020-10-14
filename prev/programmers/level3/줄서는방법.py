from math import factorial


def solution(n, k):
    answer = []
    order = list(range(0, n + 1))
    for i in range(1, n + 1):
        offset, fact = 1, factorial(n - i)
        while offset * fact < k:
            offset += 1
        answer.append(order.pop(offset))
        k -= (offset - 1) * fact
    return answer


def solution2(n, k):
    answer = []
    order = list(range(1, n+1))
    while n != 0:
        fact = factorial(n - 1)
        answer.append(order.pop(k // fact))
        n, k = n - 1, k % fact
    return answer


num = 4
for i in range(1, factorial(num) + 1):
    print(i, ":", solution(num, i))


