def solution(s):
    if len(s) % 2 == 1: return 0
    stack = []
    for ch in s:
        if stack and stack[-1] == ch: stack.pop()
        else: stack.append(ch)
    return 0 if stack else 1


print(solution('eabbacddce'))
print(solution('cdcd'))