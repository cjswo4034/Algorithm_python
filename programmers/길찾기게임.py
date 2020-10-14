from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def solution(nodeinfo):
    answer, max_x = [[], []], 0
    tree_dict = defaultdict(list)

    for v, (x, y) in enumerate(nodeinfo):
        max_x = max(max_x, x)
        tree_dict[y].append([x, v + 1])
        
    layer = sorted(tree_dict, reverse=True)         # 유효한 y 좌표
    tree = [sorted(tree_dict[l]) for l in layer]    # layer 별 좌표 집합
    order(tree, 0, tree[0][0], 0, max_x, answer)
    return answer

# layer: y, current: (x좌표, value) 
def order(tree, layer, current, l, r, res):
    if len(tree) == layer + 1: 
        res[0].append(current[1])
        res[1].append(current[1])
        return

    left, right = [], []
    for n in tree[layer + 1]:
        if l <= n[0] < current[0]: left = n
        if current[0] < n[0] <= r: right = n

    res[0].append(current[1])   # Pre-order    
    if left:  order(tree,   layer + 1,  left,   l,          current[0], res)
    if right: order(tree,   layer + 1,  right,  current[0], r,          res)
    res[1].append(current[1])   # Post-order

# 트리 구성요소
# 1) 트리는 자신의 상위 노드를 알고 있다.
# 2) 트리는 자신의 왼쪽 노드 오른쪽 노드를 알고 있다.

# 1. nodeinfo를 트리로 만든다.
#    ㄱ) 원소가 [v, x, y] 값을 갖도록 배열을 재구성한다.
#    ㄴ) y -> x 순으로 정렬한다.
#    ㄷ) y별로 층을 나눈다.
# 2. 전위 순회 한다.
# 3. 후위 순회 한다.

print(solution([[0, 100000], [1, 9999]]))