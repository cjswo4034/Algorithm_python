def solution(n, s):
    if n > s: return [-1]
    rem = s % n
    answer = [s // n for _ in range(n)]
    for i in range(rem):
        answer[n - i - 1] += 1
    return answer


print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))
