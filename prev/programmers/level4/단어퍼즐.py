# 잘푼 사람 거
def solution(strs, t):
    str_set = set(strs)
    dp = [987654] * (len(t) + 1)
    dp[0] = 0

    for i in range(1, len(t) + 1):
        for j in range(1, 6):
            if i - j >= 0 and t[i - j:i] in str_set and dp[i - j] != 987654:
                dp[i] = min(dp[i], dp[i - j] + 1)
    print(dp)
    return dp[-1]


# 통과
def solution2(strs, t):
    dp = [987654] * (len(t) + 1)
    dp[0] = 0
    dict_strs = {chr(i):[] for i in range(ord('a'), ord('z') + 1)}
    for s in strs:
        k = s[-1]
        if s not in dict_strs[k]:
            dict_strs[k].append(s)
            
    for i in range(1, len(t) + 1):
        for s in dict_strs[t[i - 1]]:
            current = t[i - len(s):i]
            if current == s and dp[i - len(s)] != 987654:
                dp[i] = min(dp[i], dp[i - len(s)] + 1)
    return dp[-1] if dp[-1] != 987654 else -1


# 시간초과(효율성 전부, 정확성 5개)
# 개선 1: 각각의 str을 일치하는 t의 위치에 표시 (DP) -> 순회하는 str에 대한 순서에 영향을 받음.
def solution1(strs, t):
    strs = sorted(strs, key=lambda x: len(x))
    answer = backtracking(strs, t, 0, 0, 987654)
    return answer if answer != 987654 else -1

def backtracking(strs, t, pos, depth, ans):
    if len(t) < pos: return 987654
    if len(t) == pos: return depth
    if depth >= ans: return ans

    res = ans
    for str in strs:
        if pos + len(str) > len(t): continue
        if t[pos: pos + len(str)] == str:
            res = min(res, backtracking(strs, t, pos + len(str), depth + 1, res))
    return res

print(solution(["ba","na","n","a"], "banana"))
print(solution("a b".split(), "bbbbba"))