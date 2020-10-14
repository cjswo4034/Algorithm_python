from itertools import combinations

import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(x)

ans = []
max_idx = 0
visit = [False for _ in range(15001)]
visit[0] = True

# * 완탐 *
# 1. 추들을 오른쪽에 올려서 나오는 무게
# 2. 1.에서 사용되지 않은 추들의 조합으로 1.을 뺀 무게
# 조합 (nCr -> n! / r!(n - r)!) 이라 불가능

# 1. 구슬과 같은 무게의 추가 있으면 가능
# 2. 구슬과 같은 무게의 추를 조합할 수 있으면 가능
# 3. 구슬에 추를 더해서 같은 무게를 방법1, 2로 구할 수 있으면 가능

# sol 2) 추를 조합해서 구슬의 무게를 구하기
# - 각 추에 대해서
# 1. visit 배열을 뒤에서부터 순회하면서 [index]가 True면 [index + 추]에 True

# sol 3) 구슬에 추를 더하기
# - 각 구슬에 대해서
# 1. visit 배열을 순회하면서 [idx + 구슬]가 True면 -> Y else N
# 2. 구슬이 추의 총 합보다 크면 N

w_len = input()
for w in map(int, input().split()):
    for idx in range(max_idx, -1, -1):
        if visit[idx]:
            visit[idx + w] = True
            max_idx = max(max_idx, idx + w)

b_len = input()
for b in map(int, input().split()):
    for idx in range(max_idx + 1):
        if idx + b > 15000:
            ans.append('N')
            break
        if visit[idx] and visit[idx + b]:
            ans.append('Y')
            break
    else: ans.append('N')

print(' '.join(list(map(str, ans))))