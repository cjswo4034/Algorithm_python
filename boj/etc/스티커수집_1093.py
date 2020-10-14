'''
*** 플레 3 (중간에서 만나기)***
- l에 대한 가치의 조합, r에 대한 가치의 조합. el + er >= k 일 때 최소 값

- 영훈이가 가지고 있는 카드가 조합에 포함된다면 -> 가격 -= 가지고 있는 카드 값
- 영훈이가 가지고 있는 카드가 조합에 포함되지 않는다면 -> 가격 -= 가지고 있는 카드 값
- 결론: 조합에 영훈이가 가진 카드가 있거나 말거나 가진 카드들의 가격을 뺀다
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = list(zip(map(int, input().split()), map(int, input().split())))   # [가격, 가치]
k = int(input())
has_money = 0       # 영훈이가 가진 카드들의 가격 총합
if int(input()): has_money = sum([arr[i][0] for i in map(int, input().split())])

l, r = arr[:n//2], arr[n//2:]
a, b = dict(), dict()
a[0], b[0] = 0, 0

def function(d, l):
    for c, w in l:
        tmp = dict()
        for k in d:
            kk = k + w
            if kk in d: tmp[kk] = min(d[kk], c + d[k])
            else: tmp[kk] = c + d[k]
        d.update(tmp)
        # d.update({k + w: c + d[k] if k + w not in d else min(d[k + w], c + d[k]) for k in d})

function(a, l)  # 왼쪽의 모든 조합
function(b, r)  # 오른쪽의 모든 조합

a = sorted(a.items())
b_keys = sorted(b.keys())
ans = 1e9
pos = len(b) - 1            # a의 가치 + b의 가치 >= k를 만족하는 b의 카드들 중 가장 낮은 가치를 가진 카드의 위치를 가리킨다
min_cost = b[b_keys[pos]]   # b[pos] ~ b[-1] 중 가장 낮은 스티커의 가격

for key, value in a:
    while key + b_keys[pos] >= k:
        ans = min(ans, value + min_cost)
        if pos == 0: break
        pos -= 1
        if key + b_keys[pos] < k:        # 이 조건 때문에 while문은 적어도 1번은 실행됨 (a[i].가치 < a[i+1].가치를 항상 만족하므로)
            pos += 1
            break
        else: min_cost = min(min_cost, b[b_keys[pos]])
        
if ans == 1e9: ans = -1
else: ans = max(0, ans - has_money)

print(ans)