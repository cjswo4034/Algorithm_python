def solution(p):
    if not p: return ''
    u, v = split(p)
    if check(u): return u + solution(v)
    return '(' + solution(v) + ')' + ''.join(['(' if pp == ')' else ')' for pp in u[1:-1]])

def split(p):
    criterion = get_criterion(p)
    return p[:criterion], p[criterion:]

def get_criterion(p):
    l = r = 0
    for pp in p:
        if pp == '(': l += 1
        else: r += 1
        if l == r: break
    return l + r

def check(p):
    cnt = 0
    for pp in p:
        if pp == '(': cnt += 1
        else: cnt -= 1
        if cnt < 0: return False
    return True

print(solution('))()()(()'))
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

if '())(':
    print(True)