def solution(p):
    if not p: return ""
    mid = next_mid(p)
    answer = get_balanced_paren(p[0:mid], p[mid:])
    return answer


def get_balanced_paren(u, v):
    if not u: return ""
    mid = next_mid(v)
    if is_balance(u):
        return u + get_balanced_paren(v[0:mid], v[mid:])
    res = "("
    if v:
        res += get_balanced_paren(v[:mid], v[mid:])
    res += ")" + reverse_paren(u)
    return res


def next_mid(p):
    l = r = 0
    for ch in p:
        if ch == '(': l += 1
        else: r += 1
        if l == r: break
    return l + r


def reverse_paren(p):
    res = ""
    for ch in p[1:-1]:
        res += '(' if ch == ')' else ')'
    return res


def is_balance(p):
    list = []
    for ch in p:
        if ch == '(':
            list.append(ch)
        elif list:
            list.pop()
        else:
            return False
    return len(list) == 0



print(solution('))()()(()'))
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

