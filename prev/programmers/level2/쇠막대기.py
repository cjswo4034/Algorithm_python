def solution(arg):
    answer = 0
    stack = 0
    for i, ch in enumerate(arg):
        if ch == '(':
            stack += 1
        else:
            stack -= 1
            if arg[i - 1] == '(':
                answer += stack
            else:
                answer += 1
    return answer

print(solution("()(((()())(())()))(())"))