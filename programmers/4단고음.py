def solution(n):
    stage = get_stage(n)
    if stage == -1 or n % 2 == 0: return 0
    
    return backtracking(1, stage, stage * 2, n)

def backtracking(value, mul, plus, n):
    if n < value: return 0
    if mul < 0 or plus < mul * 2: return 0
    if mul == 0 and plus == 0:
        return 1 if value == n else 0
    
    res = backtracking(value * 3, mul - 1, plus, n)
    res += backtracking(value + 1, mul, plus - 1, n)
    return res

def get_stage(n):
    stage, l, r = 1, 5, 5
    while stage <= 19:
        if l <= n <= r: return stage
        stage += 1
        l, r = 3 ** stage + stage * 2, r * 3 + 2
    return -1

print(solution(2147483647))