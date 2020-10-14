import re

def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '#': -1, '*': 2}
    points = re.findall('(\d+)([SDT])([*#]?)', dartResult)
    answer = [int(points[0][0]) ** bonus[points[0][1]] * option[points[0][2]]]
    for p, b, o in points[1:]:
        if o == '*': answer[-1] *= 2
        answer.append(int(p) ** bonus[b] * option[o])
    return sum(answer)


print(solution("1D2S#10S"))