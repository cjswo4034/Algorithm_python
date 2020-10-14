from itertools import permutations

def solution(expression):
    answer = 0
    expression, operator = split(expression)
    for perm in permutations([i for i in range(len(operator))]):
        result = calculate(expression, perm, operator)
        answer = max(answer, abs(result))
    return answer


def calculate(expression, priority, operator):
    n_stk, o_stk = [], []
    for e in expression:
        if e in operator:
            while o_stk and priority[operator.index(e)] <= priority[operator.index(o_stk[-1])]:
                n_stk.append(calc(o_stk.pop(), n_stk))
            o_stk.append(e)
        else:
            n_stk.append(e)
        print(n_stk, o_stk, e)
    while o_stk:
        n_stk.append(calc(o_stk.pop(), n_stk))
    return n_stk.pop()


def calc(operator, n_stk):
    operand2 = n_stk.pop()
    operand1 = n_stk.pop()
    if operator == '*':
        return operand1 * operand2
    elif operator == '+':
        return operand1 + operand2
    return operand1 - operand2


def split(expression):
    result, operator = [], set()
    num = 0
    for e in expression:
        if e.isdigit():
            num = num * 10 + int(e)
        else:
            operator.add(e)
            result.append(num)
            result.append(e)
            num = 0
    result.append(num)
    return result, list(operator)


print(solution("50*6-3*2"))
