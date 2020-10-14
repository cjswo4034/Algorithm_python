from collections import Counter

def solution(N, stages):
    acc, count = len(stages), Counter(stages)
    
    if N + 1 in count: del count[N + 1]
    for i in range(1, N + 1):
        fail = (count[i] / acc) if acc else 0
        acc -= count[i]
        count[i] = fail
        
    return sorted(count, key=lambda x: (count[x], -x), reverse=True)

# 스테이지 N 까지 순회
# 1. 스테이지에 도달했으나 클리어 하지 못한 플레이어의 수: dict[i]
# 2. 스테이지에 도달한 플레이어의 수 len(stages) - sum(dict[0 ~ i - 1])

c = Counter([1, 2, 3, 1, 1])
s = sorted(c, key=lambda x: c[x], reverse=True)
print(s)