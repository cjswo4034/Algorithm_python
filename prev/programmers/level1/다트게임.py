def solution(dart_result):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    arr, score = [], 0
    for ch in dart_result:
        if str.isalpha(ch):
            score **= bonus[ch]
            arr.append(score)
            score = 0
        elif ch == '*':
            arr[-2:] = [i * 2 for i in arr[-2:]]
        elif ch == '#':
            arr[-1] = arr[-1] * -1
        else:
            score = score * 10 + int(ch)
    return sum(arr)


def solution_regex(dart_result):
    import re

    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([#*]?)')
    dart = p.findall(dart_result)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    return sum(dart)


print(solution_regex('1S2D*3T'))
print(solution_regex('1D2S#10S'))
print(solution_regex('1D2S0T'))
print(solution_regex('1S*2T*3S'))
print(solution_regex('1D#2S*3S'))
print(solution_regex('1T2D3D#'))
print(solution_regex('1D2S3T*'))
