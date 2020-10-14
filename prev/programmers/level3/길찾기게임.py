import sys
sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, value, x):
        self.value = value
        self.x = x
        self.l = None
        self.r = None

    def insert(self, x, value):
        if self.x > x:
            if self.l is None: self.l = Node(value, x)
            else: self.l.insert(x, value)
        else:
            if self.r is None: self.r = Node(value, x)
            else: self.r.insert(x, value)


def solution(node_info):
    answer = [[], []]
    for i, node in enumerate(node_info):
        node.append(i + 1)
    node_info.sort(key=lambda x: (-x[1], x[0]))

    root = Node(node_info[0][2], node_info[0][0])
    for i in range(1, len(node_info)):
        root.insert(node_info[i][0], node_info[i][2])

    order(root, answer)
    return answer


def order(node, answer):
    if node is None: return
    answer[0].append(node.value)
    order(node.l, answer)
    order(node.r, answer)
    answer[1].append(node.value)


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))