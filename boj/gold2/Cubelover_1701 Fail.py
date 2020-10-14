# str[i:i + size + 1]이 2면 str[i:i + size], str[i+1:i+size+1]도 2다
# i+size == j -> s[i:i+size] == s[i:j], s[i:j] == s[j:j+size] -> s[i:j+size] == s[i:j] * 2
from collections import defaultdict

import sys

input = sys.stdin.readline

# aaaaaaaaaaaaaaaaaaaaa에서 틀림...

s = input()
prev = defaultdict(list)
for i in range(len(s)): 
    if s.count(s[i]) > 1: prev[s[i]].append(i)

candidates = defaultdict(list)  # aaaaaaa와 같은 연속적인 문자

for k in prev:
    copy_arr = []

    i, j = 0, 0
    while i < len(prev[k]):
        j = i + 1
        while j < len(prev[k]):
            if prev[k][j - 1] + 1 != prev[k][j]: break
            j += 1

        length = j - i
        if length > 2:
            candidates[length].append(prev[k][i])
            i = j - 1   # 연속적인 문자가 끝나는 위치 ex. aaaaa -> j =4
        else: 
            copy_arr.append(prev[k][i])
            i += 1

    if len(copy_arr) > 1: prev[k] = copy_arr
    else: prev[k] = []

ans = 1 if prev else 0

for size in range(2, len(s)):
    next = defaultdict(list)
    if size + 1 in candidates:
        for idx in candidates[size + 1]:
            next[s[idx:idx + size]].extend([idx, idx + 1])
        del candidates[size + 1]
        
    for k in prev:
        while prev[k]:
            flag = False
            src = prev[k].pop(0)
            
            while prev[k] and src + size > len(s): src = prev[k].pop(0)
            if not prev[k]: continue

            src_str = s[src + size - 1]
            for _ in range(len(prev[k])):
                dest = prev[k].pop(0)
                if dest + size > len(s): continue

                if src_str == s[dest + size - 1]:
                    flag = True
                    next[k + src_str].append(dest)
                else: prev[k].append(dest)
            if flag: next[k + src_str].append(src)
        
    prev = next
    if prev: ans = max(ans, size)
    if not prev and not candidates: break

print(ans)