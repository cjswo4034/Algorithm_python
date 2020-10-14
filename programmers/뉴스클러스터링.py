from collections import Counter
import re

def solution(str1, str2):
    str1 = slice(str1)
    str2 = slice(str2)
    
    cnt1 = Counter(str1)
    cnt2 = Counter(str2)
    
    set1 = set(str1)
    set2 = set(str2)
    
    sub = set1 & set2
    union = set1 | set2

    if len(sub) == 0: return 65536 if len(union) == 0 else 0
    else:
        l1 = sum([min(cnt1[s], cnt2[s]) for s in sub])  # Counter 자료형은 없으면 0을 반환
        l2 = sum([max(cnt1[s], cnt2[s]) for s in union])
        return int(l1 / l2 * 65536)

def slice(s):
    s = re.findall('[a-z]{2,}', s.lower())
    res = []
    for ss in s:
        if len(ss) < 2: continue
        for i in range(len(ss) - 1):
            res.append(ss[i:i + 2])
    return res

def slice2(s):
    s = re.replace(s.lower(), '[^a-z]')
    res = []
    for i in range(len(s) - 1):
        tmp = s[i:i + 2]
        if ' ' not in tmp: res.append(tmp)
    return res

print(solution('aaabbb', 'aa bbbbdc'))