def solution(operations):
    q = []

    for operation in operations:
        if operation[0] == 'I':
            q.append(int(operation[2:]))
            continue
        if not q: continue
        if operation.find('-') > 0:
            q.sort()  # operator, operand 분리해서 q.remove(operand)로 변경
        else:
            q.sort(reverse=True)
        q.pop(0)

    if not q: return [0, 0]
    return [max(q), q[0]]


print(solution([
    "I -45",
    "I 653",
    "D 1",
    "I -642",
    "I 45",
    "I 97",
    "D 1",
    "D -1",
    "I 333"]))
