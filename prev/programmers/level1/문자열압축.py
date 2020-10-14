def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, get_dict(s, i))
    return answer


def get_dict(s, n):
    ans, prev, cnt = "", "", 1
    for i in range(0, len(s), n):
        if prev == s[i:i+n]:
            cnt += 1
        else:
            ans += prev if cnt == 1 else str(cnt) + prev
            prev = s[i:i+n]
            cnt = 1

    if not len(s) % n:
        ans += prev if cnt == 1 else str(cnt) + prev
    else:
        ans += s[-(len(s) % n):]
    return len(ans)


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))