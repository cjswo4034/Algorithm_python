def solution(s):
    answer = 0

    for i in range(len(s), 0, -1):
        for j in range(0, len(s) - i + 1):
            if is_penlindrome(s[j:j + i]): return i
    return answer


def is_penlindrome(str):
    return str == str[::-1]


print(solution("abcdcba"))
print(solution("abccbaa"))