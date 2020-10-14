import re
from collections import Counter

def solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

def solution2(s):
    answer = []

    s = s.lstrip('{').rstrip('}').split('},{')
    for idx in range(len(s)):
        s[idx] = list(map(int, s[idx].split(',')))

    s, se = sorted(s, key=len), set()
    
    for row in s:
        for el in row:
            if el in se: continue
            answer.append(el)
            se.add(el)
            
    return answer

## ,가 없으면 크기가 1인 튜플.
## 1. '},{'로 문자열을 쪼갠다 
## 2. 각각의 배열에 }과 {를 없앤다.
## 3. 배열의 ,를 없앤다.


print(solution2("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{123}}"))