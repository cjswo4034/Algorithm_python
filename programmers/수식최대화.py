from itertools import permutations
import re

def solution2(expression):
    operands, values = [list(p) for p in permutations(['-', '+', '*'])], []
    expression = re.split(r'(\D)', expression)

    for op in operands:
        ex = expression[:]
        for p in op:
            while p in ex:
                idx = ex.index(p)
                ex[idx - 1] = str(eval(ex[idx - 1] + ex[idx] + ex[idx + 1]))
                ex = ex[:idx] + ex[idx + 2:]
        values.append(ex[-1])
    return max([abs(int(v)) for v in values])
    
def solution(expression):
    expression = split(expression)
    answer, sign = 0, ['+', '*', '-']
    for p in permutations(range(3)):
        priority = dict()
        for i in range(3):
            priority[sign[i]] = p[i]
        answer = max(answer, calculate(expression, priority))
    return answer

def calculate(expression, priority):
    values, operands = [], []
    for e in expression:
        if type(e) is int: values.append(e)
        else:
            curr_priority = priority[e]
            while operands and priority[operands[-1]] >= curr_priority:
                values.append(function(values.pop(-2), values.pop(), operands.pop()))
            operands.append(e)

    while operands:
        values.append(function(values.pop(-2), values.pop(), operands.pop()))
    return abs(values[0])

def function(v1, v2, op):
    if op == '+': return v1 + v2
    elif op == '*': return v1 * v2
    else: return v1 - v2

def split(expression):
    res = []
    num = re.split('[\\D]', expression)
    sign = re.split('[\\d]+', expression)
    res.append(int(num[0]))
    for i in range(1, len(num)):
        res.append(sign[i])
        res.append(int(num[i]))
    return res

expression = "100-200*300-500+20"
print(solution(expression))