import re

def solution(s):
    answer = []
    comp = re.compile('\d+')
    arr = s.split(',{')
    arr.sort(key = len)
    for el in arr:
        numbers = comp.findall(el)
        for number in numbers:
            number = int(number)
            if number not in answer:
                answer.append(number)
    return answer

print(solution("{{2,1234},{2},{2,1234,3},{2,1234,3,4}}"))

# ({}((n - i) * 2))